#!/bin/bash
PREFIX="https://github.com/ianand75/zro-sybil-icfa/tree/main/clusters/"
index=1

for file in ../clusters/*; do
    
    filename=$(basename "$file")
    echo -e "[Cluster #$index: $filename]($PREFIX$filename)\n"
    # Increment the index
    ((index++))
done
