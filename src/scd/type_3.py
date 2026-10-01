from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder \
    .appName("SCD Type 3") \
    .getOrCreate()

# Define schema
schema = StructType([
    StructField("customer_id", IntegerType()),
    StructField("name", StringType()),
    StructField("current_city", StringType()),
    StructField("previous_city", StringType())
])

# Existing customer data
target_data = [
    (1, "Rahul", "Delhi", None),
    (2, "Amit", "Mumbai", None),
    (3, "Neha", "Pune", None)
]

target_df = spark.createDataFrame(
    target_data,
    schema
)

target_df.show()

# Incoming customer data
source_data = [
    (1, "Rahul", "Bengaluru"),
    (2, "Amit", "Mumbai"),
    (3, "Neha", "Chennai")
]

source_df = spark.createDataFrame(
    source_data,
    ["customer_id", "name", "city"]
)

source_df.show()

# Join target and source
t = target_df.alias("t")
s = source_df.alias("s")

df2 = s.join(
    t,
    s.customer_id == t.customer_id,
    "left"
)

# Update previous city and current city
df3 = df2.select(
    col("s.customer_id").alias("customer_id"),
    col("s.name").alias("name"),
    col("s.city").alias("current_city"),
    when(
        col("s.city") != col("t.current_city"),
        col("t.current_city")
    ).otherwise(
        col("t.previous_city")
    ).alias("previous_city")
)

df3.show()

spark.stop()