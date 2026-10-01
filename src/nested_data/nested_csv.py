from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    ArrayType
)
from pyspark.sql.functions import explode

spark = SparkSession.builder \
    .appName("Nested Data") \
    .getOrCreate()

# Define schema
schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("skills", ArrayType(StringType()))
])

# Create data
data = [
    (1, "Rahul", ["Python", "SQL", "Spark"]),
    (2, "Amit", ["Java", "SQL"]),
    (3, "Neha", ["Python", "Spark"])
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

df.printSchema()
df.show(truncate=False)

# Explode skills
df2 = df.select(
    "id",
    "name",
    explode("skills").alias("skill")
)

df2.show()

spark.stop()