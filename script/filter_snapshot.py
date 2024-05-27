# Import SparkSession
from pyspark.sql import SparkSession
from os import path as osp
from mako.template import Template
import sys

# Create SparkSession 
spark = SparkSession.builder.config("spark.executor.memory", "8g").master("local[*]").appName("snapshot") .getOrCreate() 


out_dir = "data_snapshot_filtered"
snapshot = "data_snapshot_0515"
initial_sybil_list = "initialList.csv"

spark.read.csv(snapshot, header=True).createTempView("snapshot")
spark.read.csv(initial_sybil_list, header=True).createTempView("initial")

# find out how many messages sent for each wallet address.
spark.sql("select SENDER_WALLET as address, count(SOURCE_TRANSACTION_HASH) as messages from snapshot group by SENDER_WALLET order by messages desc").createOrReplaceTempView("snapshot_group_by_address")

# filter out initial sybil addresses.
df = spark.sql("select * from snapshot_group_by_address where address not in (select address from initial)")

df.write.csv(out_dir, header=True)

spark.stop()