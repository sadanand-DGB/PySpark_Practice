from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("With Column Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Add a new column
df2 = df.withColumn("annual_salary", df.salary * 12)

# Display data
print("Employees Data:")
df2.show()

# Stop Spark
spark.stop() 