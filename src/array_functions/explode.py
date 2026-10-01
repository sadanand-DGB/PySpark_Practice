from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    explode,
    explode_outer,
    posexplode,
    posexplode_outer
)

spark = SparkSession.builder \
    .appName("Explode Functions") \
    .getOrCreate()

data = [
    (1, "Rahul", ["Python", "SQL", "Spark"]),
    (2, "Amit", ["Java", "SQL"]),
    (3, "Neha", None)
]

df = spark.createDataFrame(
    data,
    ["id", "name", "skills"]
)

# explode
df2 = df.select(
    "id",
    "name",
    explode("skills").alias("skill")
)

df2.show()

# explode_outer
df3 = df.select(
    "id",
    "name",
    explode_outer("skills").alias("skill")
)

df3.show()

# posexplode
df4 = df.select(
    "id",
    "name",
    posexplode("skills").alias("position", "skill")
)

df4.show()

# posexplode_outer
df5 = df.select(
    "id",
    "name",
    posexplode_outer("skills").alias("position", "skill")
)

df5.show()

spark.stop()