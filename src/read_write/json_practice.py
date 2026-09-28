from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("JSON Practice") \
    .getOrCreate()

# Read JSON
df = spark.read \
    .option("multiLine", True) \
    .option("inferSchema", True) \
    .json("src/utils/employees.json")

# Display data
print("Employees Data:")
df.show()

# Display schema
print("Schema:")
df.printSchema()


# Write JSON
df.write \
    .mode("overwrite") \
    .json("src/utils/employees_output_json")


# Stop Spark
spark.stop()