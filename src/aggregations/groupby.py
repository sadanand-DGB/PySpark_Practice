from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("GroupBy Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Group employees by department
df2 = df.groupBy("department_id").count()

# Display data
print("Employees by Department:")
df2.show()

# Stop Spark
spark.stop()