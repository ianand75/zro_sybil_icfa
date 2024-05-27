import os
import shutil
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

import glob
from mako.template import Template
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np  # Add this import for cosine and sine functions
import plotly.graph_objects as go
import plotly.io as pio


clusters_dir = "output1"

# Define template and parent directory
template_file = "proof_cross.template.md"
proof_template = Template(filename=template_file)
parent_directory = clusters_dir



def cluster_chain(cluster_id):
    return cluster_id.split('-')[0]

def cluster_size(cluster_id):
    return int(cluster_id.split('-')[2])

def cluster_funder(cluster_id):
    return cluster_id.split('-')[3]

def read_trans(filepath): 
    with open(filepath, "r") as file:
        start_storing = False
        lines_after_target = []
        for line in file:
            if "# Transactions that executed the fund transfer" in line:
                start_storing = True
                continue
            if start_storing:
                lines_after_target.append(line.strip())
    return "\n".join(lines_after_target)

# Function to shorten addresses
def shorten_address(address, length=6):
    if len(address) <= length * 2:
        return address
    return f"{address[:length]}...{address[-length:]}"



def create_graph(class_members, output_path):
    G = nx.DiGraph()
    address_map = {}
    labels = {}

    funders = set()
    addresses = set()

    for i, cluster_id in enumerate(class_members):
        chain = cluster_chain(cluster_id)
        funder = cluster_funder(cluster_id)
        funder_label = f"{chain}-{funder}"
        funders.add(funder_label)

        labels[funder_label] = funder_label
        G.add_node(funder_label)

        address_messages_file = os.path.join(clusters_dir, cluster_id, "address.csv")
        df = pd.read_csv(address_messages_file)
        for index, row in df.iterrows():
            address = row['address']
            shortened_address = address
            address_map[address] = shortened_address
            labels[shortened_address] = shortened_address
            addresses.add(shortened_address)
            G.add_node(shortened_address)
            G.add_edge(funder_label, shortened_address)

    # Arrange funders inside a circle
    num_funders = len(funders)
    funder_angle_step = 360 / num_funders if num_funders > 0 else 0
    funder_radius = 10

    funder_positions = {}
    for i, funder in enumerate(funders):
        angle = i * funder_angle_step
        radian = np.radians(angle)
        x = funder_radius * 0.5 * (i % 2 + 1) * np.cos(radian)
        y = funder_radius * 0.5 * (i % 2 + 1) * np.sin(radian)
        funder_positions[funder] = (x, y)

    # Define circular strip parameters
    strip_radius = 30
    strip_width = 5

    # Randomly position addresses within the circular strip
    address_positions = {}
    for address in addresses:
        theta = random.uniform(0, 2 * np.pi)  # Random angle within the strip
        r = random.uniform(strip_radius - strip_width / 2, strip_radius + strip_width / 2)  # Random radius within the strip
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        address_positions[address] = (x, y)

    pos = {**funder_positions, **address_positions}

    # Assign unique colors to each funder
    colors = plt.cm.tab20(range(len(funders)))

    # Create interactive graph using Plotly
    fig = go.Figure()

    # Add edges and nodes with unique colors for each funder
    funder_to_color = {funder: f"rgb({int(color[0]*255)}, {int(color[1]*255)}, {int(color[2]*255)})" for funder, color in zip(funders, colors)}

    for edge in G.edges():
        funder = edge[0]
        edge_color = 'grey' #funder_to_color[funder]
        fig.add_trace(go.Scatter(
            x=[pos[edge[0]][0], pos[edge[1]][0]],
            y=[pos[edge[0]][1], pos[edge[1]][1]],
            mode='lines',
            line=dict(width=0.5, color=edge_color),
            hoverinfo='none'
        ))

    for node in G.nodes():
        node_color = 'skyblue'
        node_size = 10
        if node in funders:
            node_size = 20
            node_color = 'blue'
        fig.add_trace(go.Scatter(
            x=[pos[node][0]],
            y=[pos[node][1]],
            mode='markers',
            marker=dict(symbol='circle', size=node_size, color=node_color),
            text=[labels[node]],
            hoverinfo='text'
        ))

    # Set layout
    fig.update_layout(
        title='Cluster Visualization',
        titlefont_size=16,
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=40),
        annotations=[dict(
            text="Python code: <a href='https://github.com/plotly/plotly.py'> https://github.com/plotly/plotly.py</a>",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.005, y=-0.002
        )],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    fig.write_html(output_path + ".html")  # Save interactive HTML version
    # fig.write_image(output_path + "_plotly.png", format="png", width=1200, height=1200)  # Save PNG version



def add_nodes_and_edges(G, df):
    rows = df.collect()
    for row in rows:
        dataset_id1 = row.dataset_id1
        dataset_id2 = row.dataset_id2
        count = int(row.intersection_count)
        funder1 = cluster_funder(row.dataset_id1)
        funder2 = cluster_funder(row.dataset_id2)

        if funder1 == funder2 and count >= 10:
            G.add_node(dataset_id1, funder=funder1)
            G.add_node(dataset_id2, funder=funder2)
            G.add_edge(dataset_id1, dataset_id2, weight=count)

def infer_classes_from_intersections(intersect_df):
   
    
    # Initialize the graph
    G = nx.Graph()

    # Add nodes and edges to the graph based on the intersection data
    add_nodes_and_edges(G, intersect_df)

    # Find connected components in the graph
    components = list(nx.connected_components(G))

    # Group datasets by their connected components
    inferred_classes = {}
    for component in components:
        funders = {G.nodes[node]['funder'] for node in component}
        if len(funders) == 1:  # Ensure all nodes in the component share the same funder
            inferred_classes[list(funders)[0]] = list(component)

    return inferred_classes


# Initialize SparkSession
spark = SparkSession.builder.appName("CreateClasses").getOrCreate()

# Read the relations from CSV files
equal_df = spark.read.csv("overlap/equal_relations.csv", header=True)
subsetOf_df = spark.read.csv("overlap/subset_relations.csv", header=True)
intersect_df = spark.read.csv("overlap/overlap_relations.csv", header=True)


# Union-Find implementation
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
            self.rank[item] = 0
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

uf = UnionFind()

# Process equal and subset relations
for row in equal_df.collect():
    uf.union(row['dataset_id1'], row['dataset_id2'])
for row in subsetOf_df.collect():
    uf.union(row['subset_dataset_id'], row['superset_dataset_id'])

# Extract classes
classes = {}
for dataset_id in uf.parent.keys():
    root = uf.find(dataset_id)
    if root not in classes:
        classes[root] = []
    classes[root].append(dataset_id)


classes2 = infer_classes_from_intersections(intersect_df=intersect_df)

classes = {**classes, **classes2}


print(classes)

# Process each class
index = 1
for class_root, class_members in classes.items():
    proofs = []
    merged_df = None

    # Union clusters
    for cluster_id in class_members:
        this_cluster_dir = os.path.join(clusters_dir, cluster_id)
        address_messages_file =  os.path.join(this_cluster_dir, "address-messages.csv")
        df = spark.read.csv(address_messages_file, header=True, inferSchema=True)
        merged_df = df if merged_df is None else merged_df.union(df).distinct()
        proof_file = os.path.join(this_cluster_dir, "proof.md")
        proofs.append({"chain": cluster_chain(cluster_id), "count": cluster_size(cluster_id), "funder": cluster_funder(cluster_id), "tx": read_trans(proof_file)})


    count = merged_df.count()

    new_directory_name = f"cross-{index}-{count}"
    new_directory_path = os.path.join(parent_directory, new_directory_name)
    os.makedirs(new_directory_path)
    

    new_proof_file = os.path.join(new_directory_path, "proof.md")
    proof = proof_template.render(proofs=proofs, count=count)
    with open(new_proof_file, "w") as file:
        file.write(proof)

    address_only_df = merged_df.select("address").toPandas()
    address_only_df.to_csv(os.path.join(new_directory_path, "addresses.csv"), index=False)
    merged_df.toPandas().to_csv(os.path.join(new_directory_path, "address-messages.csv"), index=False)

    # Create and save the graph for the class
    graph_output_path = os.path.join(new_directory_path, "visualization")
    create_graph(class_members, graph_output_path)

    index += 1

for class_root, class_members in classes.items():
    for cluster_id in class_members:
        this_cluster_dir = os.path.join(clusters_dir, cluster_id)
        os.system("rm -rf " + this_cluster_dir)

print("Processing complete. New directories and files created.")
spark.stop()
