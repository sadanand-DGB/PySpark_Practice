from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Filter Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Filter employees with salary greater than 50000
filter_df = df.filter(df.salary > 50000)

# Display data
print("Filtered Employees:")
filter_df.show()

# Stop Spark
spark.stop()