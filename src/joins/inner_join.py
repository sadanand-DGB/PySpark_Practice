from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Inner Join Practice") \
    .getOrCreate()

# Read employees
employees = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Read department
department = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/department.csv")

# inner join
df2 = employees.join(
    department,
    employees.department_id == department.department_id,
    "inner"
)


# Display data
print("Inner Join:")
df2.show()

# Stop Spark
spark.stop()