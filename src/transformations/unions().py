from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Union Practice") \
    .getOrCreate()

data1 = [
    (1, "Rahul"),
    (2, "Amit")
]

data2 = [
    (3, "Neha"),
    (4, "Priya")
]

df1 = spark.createDataFrame(
    data1,
    ["id", "name"]
)

df2 = spark.createDataFrame(
    data2,
    ["id", "name"]
)

# union
df3 = df1.union(df2)

print("Union:")
df3.show()

# unionAll
df4 = df1.unionAll(df2)

print("Union All:")
df4.show()

# Change column order for unionByName
df5 = df2.select(
    "name",
    "id"
)

# unionByName
df6 = df1.unionByName(df5)

print("Union By Name:")
df6.show()

spark.stop()