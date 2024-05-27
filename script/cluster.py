# Import SparkSession
from pyspark.sql import SparkSession
from os import path as osp
import os
from mako.template import Template
import sys

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np  # Add this import for cosine and sine functions
import plotly.graph_objects as go
import plotly.io as pio


def create_graph(chain, funder, addresses_df,  output_path):
    G = nx.DiGraph()
    address_map = {}
    labels = {}

    funders = set()
    addresses = set()

    funder_label = f"{chain}-{funder}"
    funders.add(funder_label)

    labels[funder_label] = funder_label
    G.add_node(funder_label)

    
    for row in addresses_df.collect():
        address = row[0]
        address_map[address] = address
        labels[address] = address
        addresses.add(address)

        G.add_node(address)
        G.add_edge(funder_label, address)
            

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

    fig.write_html(output_path)  # Save interactive HTML version
    # fig.write_image(output_path + "_plotly.png", format="png", width=1200, height=1200)  # Save PNG version



# Create SparkSession 
spark = SparkSession.builder.config("spark.executor.memory", "8g").master("local[*]").appName("cluster") .getOrCreate() 


chain = sys.argv[1]

if chain == None: 
    sys.exit(1)

chains = {
    "arb" : {
        "name": "Arbitrium One",
        "scan": "https://arbiscan.io/tx"
    },

    "op" : {
        "name": "OP Mainnet",
        "scan": "https://optimistic.etherscan.io/tx"
    },
    "polygon" : {
        "name": "Polygon Mainnet",
        "scan": "https://polygonscan.com/tx"
    },

    "bsc" : {
        "name": "BSC Mainnet",
        "scan": "https://bscscan.com/tx"
    },
    "celo" : {
        "name": "Celo Mainnet",
        "scan": "https://celoscan.io/tx"
    },

    "fantom" : {
        "name": "Fantom",
        "scan": "https://ftmscan.com/tx"
    },

    "moonriver" : {
        "name": "MoonRiver",
        "scan": "https://moonriver.moonscan.io/tx"
    },

    "gnosis" : {
        "name": "Gnosis",
        "scan": "https://gnosisscan.io/tx"
    },

    "ok" : {
        "name": "OKChain",
        "scan": "https://www.oklink.com/oktc/tx"
    },
}

chain_name = chains[chain]['name']
scan_url = chains[chain]['scan']


snapshot_dir = "data_snapshot_filtered"
trans_data_dir = "data_direct_relations"

output_dir = "output1"

proof_template_file = "proof.template.md"
proof_output_file = "proof.md"

proof_template = Template(filename=proof_template_file)

spark.read.csv(snapshot_dir, header=True).createTempView("snapshot_clean")
spark.read.csv(osp.join(trans_data_dir, chain), header=True).createTempView("trans")

spark.sql("select trans.from as funder, snapshot_clean.address as address, snapshot_clean.messages as messages from snapshot_clean join trans on snapshot_clean.address=trans.to").createOrReplaceTempView("snapshot_funder")

spark.sql("select funder, count(address) as count from snapshot_funder group by funder order by count desc").createOrReplaceTempView("cluster")

df = spark.sql("select * from cluster where count>30")

# print(df.count())

funders = df.select("funder").collect()

i = 0
for f in funders: 
    # print(f.funder)
    i += 1
    funder = f.funder
    group = spark.sql("select distinct address, messages from snapshot_funder where funder='" + funder + "'")
    count = group.count()
    if count <= 20: 
        continue
    
    cluster_id = chain + "-" + str(i) + "-" + str(count) + "-" + funder
    dir = osp.join(output_dir, cluster_id)
    os.makedirs(dir, exist_ok=True)

    address_messages_csv = osp.join(dir, "address-messages.csv")
    group.toPandas().to_csv(address_messages_csv, index=False)
    # group.coalesce(1).write.option('header', True).csv(dir)

    addresses = group.select("address")
    address_csv = osp.join(dir, "address.csv")
    addresses.toPandas().to_csv(address_csv, index=False)

    txRecords = spark.sql("select distinct tx from trans where from='" + funder + "'").collect()
    tx = '\n'.join([osp.join(scan_url, s.tx) for s in txRecords])

    proof = proof_template.render(chain_name=chain_name, funder=funder, count=count, tx=tx)
    with open(osp.join(dir,proof_output_file), "w") as file:
        file.write(proof)
    
    create_graph(chain=chain, funder=funder, addresses_df=addresses, output_path=osp.join(dir, "visualization.html"))

spark.stop()

    



