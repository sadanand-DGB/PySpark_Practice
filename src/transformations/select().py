from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Select Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Select columns
select_df = df.select("name", "salary")

# Display data
print("Selected Columns:")
select_df.show()

# Stop Spark
spark.stop()