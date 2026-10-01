from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_date
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DateType
)


spark = SparkSession.builder \
    .appName("SCD Type 2") \
    .getOrCreate()


# Define target schema
target_schema = StructType([
    StructField("customer_id", IntegerType()),
    StructField("name", StringType()),
    StructField("city", StringType()),
    StructField("start_date", StringType()),
    StructField("end_date", StringType()),
    StructField("is_current", StringType())
])


# Existing SCD2 target table
target_data = [
    (1, "Rahul", "Delhi", "2026-01-01", None, True),
    (2, "Amit", "Mumbai", "2026-01-01", None, True)
]

target_df = spark.createDataFrame(
    target_data,
    target_schema
)

# Incoming source data
source_data = [
    (1, "Rahul", "Pune"),
    (3, "Neha", "Chennai")
]

source_df = spark.createDataFrame(
    source_data,
    ["customer_id", "name", "city"]
)

# Get current records from target
t = target_df.filter(
    col("is_current") == True
).alias("t")

s = source_df.alias("s")

# Compare source with current target
df2 = s.join(
    t,
    s.customer_id == t.customer_id,
    "left"
)

# Changed customers
changed = df2.filter(
    col("t.customer_id").isNotNull() &
    (col("s.city") != col("t.city"))
)

# New customers
new = df2.filter(
    col("t.customer_id").isNull()
)

# Keep unchanged target records
unchanged = target_df.filter(
    col("is_current") == True
).join(
    changed.select(
        col("s.customer_id").alias("customer_id")
    ),
    "customer_id",
    "left_anti"
)

# Close old version
old_version = changed.select(
    col("t.customer_id").alias("customer_id"),
    col("t.name").alias("name"),
    col("t.city").alias("city"),
    col("t.start_date").alias("start_date"),
    current_date().alias("end_date"),
    lit(False).alias("is_current")
)

# Insert new version
new_version = changed.select(
    col("s.customer_id").alias("customer_id"),
    col("s.name").alias("name"),
    col("s.city").alias("city"),
    current_date().alias("start_date"),
    lit(None).cast("date").alias("end_date"),
    lit(True).alias("is_current")
)

# Insert new customers
new_customer = new.select(
    col("s.customer_id").alias("customer_id"),
    col("s.name").alias("name"),
    col("s.city").alias("city"),
    current_date().alias("start_date"),
    lit(None).cast("date").alias("end_date"),
    lit(True).alias("is_current")
)

# Final SCD2 table
df3 = unchanged \
    .unionByName(old_version) \
    .unionByName(new_version) \
    .unionByName(new_customer)

df3.orderBy("customer_id", "start_date").show()

spark.stop()