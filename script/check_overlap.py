from pyspark.sql import SparkSession
import os
from itertools import combinations

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SubsetCheck") \
    .getOrCreate()

# Path to the clusters directory
clusters_path = "output"

# Load all datasets from the clusters directory
clusters = {}
for subdir, _, files in os.walk(clusters_path):
    dataset_id = os.path.basename(subdir)
    dataset_dfs = []
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            df = spark.read.csv(file_path, header=True, inferSchema=True)
            dataset_dfs.append(df)
    if dataset_dfs:
        clusters[dataset_id] = dataset_dfs

def check_relation(df1, df2):
    """Check the relationship between two DataFrames."""
    if df1.count() == df2.count() and df1.subtract(df2).isEmpty() and df2.subtract(df1).isEmpty():
        return "=="
    elif df1.count() < df2.count() and df1.subtract(df2).isEmpty():
        return "<"
    elif df2.count() < df1.count() and df2.subtract(df1).isEmpty():
        return ">"
    else:
        intersection_count = df1.intersect(df2).count()
        if intersection_count > 0:
            return f"<{intersection_count}>"
        else:
            return "No relation"

# Lists to hold the relations
equal = []
subsetOf = []
overlap = []

# Dictionary to track processed datasets
processed = {}

# Check relations between all pairs of DataFrames
for (dataset_id1, dfs1), (dataset_id2, dfs2) in combinations(clusters.items(), 2):
    if dataset_id1 not in processed and dataset_id2 not in processed:
        relation = check_relation(dfs1[0], dfs2[0])
        if relation != "No relation":
            print(f"{dataset_id1} {relation} {dataset_id2}:")
            if relation == "==":
                equal.append((dataset_id1, dataset_id2))
                processed[dataset_id1] = True  # Mark dataset_id1 as processed
            elif relation == "<":
                subsetOf.append((dataset_id1, dataset_id2))
                processed[dataset_id1] = True  # Mark dataset_id1 as processed
            elif relation == ">":
                subsetOf.append((dataset_id2, dataset_id1))
                processed[dataset_id2] = True  # Mark dataset_id2 as processed
            elif "<" in relation:
                intersection_count = int(relation.strip("<>"))
                overlap.append((dataset_id1, dataset_id2, intersection_count))

# Create DataFrames for the relations
equal_df = spark.createDataFrame(equal, ["dataset_id1", "dataset_id2"])
subsetOf_df = spark.createDataFrame(subsetOf, ["subset_dataset_id", "superset_dataset_id"])
overlap_df = spark.createDataFrame(overlap, ["dataset_id1", "dataset_id2", "intersection_count"])

# Display the result DataFrames
print("Equal Relations:")
equal_df.show()

print("Subset Relations:")
subsetOf_df.show()

print("Overlap Relations:")
overlap_df.show()

# Optionally, save the DataFrames to files
equal_df.write.csv("equal_relations.csv", header=True)
subsetOf_df.write.csv("subset_relations.csv", header=True)
overlap_df.write.csv("overlap_relations.csv", header=True)

# Stop SparkSession
spark.stop()
