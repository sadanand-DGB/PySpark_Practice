from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Semi Join Practice") \
    .getOrCreate()

# Read employees
employees = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Read departments
departments = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/department.csv")

# Create aliases
e = employees.alias("e")
d = departments.alias("d")

# Perform semi join
df2 = e.join(
    d,
    e.department_id == d.department_id,
    "left_semi"
)

# Display data
print("Semi Join:")
df2.show()

# Stop Spark
spark.stop()