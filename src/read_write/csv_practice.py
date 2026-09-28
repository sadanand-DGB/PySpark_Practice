from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("CSV Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Display data
print("Employees Data:")
df.show()

# Display schema
print("Schema:")
df.printSchema()



# Write CSV
df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("src/utils/employees_output")