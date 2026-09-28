from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Parquet Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Write Parquet
df.write \
    .mode("overwrite") \
    .parquet("src/utils/employees_parquet")

# Read Parquet
parquet_df = spark.read \
    .parquet("src/utils/employees_parquet")

# Display data
print("Employees Data:")
parquet_df.show()

# Display schema
print("Schema:")
parquet_df.printSchema()

# Stop Spark
spark.stop()