# !/bin/bash

for file in ./*.gz; do 
	gzip -d -r $file
done

