from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create Spark session
spark = SparkSession.builder \
    .appName("Explicit Schema Practice") \
    .getOrCreate()

# Define schema
schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department_id", IntegerType(), True),
    StructField("salary", IntegerType(), True)
])

# Read CSV with explicit schema
df = spark.read \
    .option("header", True) \
    .schema(schema) \
    .csv("src/utils/employees.csv")

# Display data
print("Employees Data:")
df.show()

# Display schema
print("Schema:")
df.printSchema()

# Stop Spark
spark.stop()