from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Left Join Practice") \
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

# Create aliases
e = employees.alias("e")
d = department.alias("d")

# Perform left join
df2 = e.join(
    d,
    e.department_id == d.department_id,
    "left"
)

# Apply filter
df2 = df2.filter(e.salary > 50000)

# Display data
print("Left Join:")
df2.show()

# Stop Spark
spark.stop()