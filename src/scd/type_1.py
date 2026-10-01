from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce

spark = SparkSession.builder \
    .appName("SCD Type 1 Practice") \
    .getOrCreate()

# Existing target data
target_data = [
    (1, "Rahul", "Delhi"),
    (2, "Amit", "Mumbai"),
    (3, "Neha", "Pune")
]

target_df = spark.createDataFrame(
    target_data,
    ["customer_id", "name", "city"]
)

# New incoming source data
source_data = [
    (1, "Rahul", "Bangalore"),
    (2, "Amit", "Mumbai"),
    (4, "Shivam", "Chennai")
]

source_df = spark.createDataFrame(
    source_data,
    ["customer_id", "name", "city"]
)

print("Target:")
target_df.show()

print("Source:")
source_df.show()

# Alias DataFrames
t = target_df.alias("t")
s = source_df.alias("s")

# Join source and target
df2 = t.join(
    s,
    t.customer_id == s.customer_id,
    "full"
)

# Apply SCD Type 1 logic
df3 = df2.select(
    coalesce(s.customer_id, t.customer_id).alias("customer_id"),
    coalesce(s.name, t.name).alias("name"),
    coalesce(s.city, t.city).alias("city")
)

print("SCD Type 1 Result:")
df3.show()

spark.stop()