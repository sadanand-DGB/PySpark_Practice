from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg, max, min , countDistinct,first,last,collect_list,collect_set

# Create Spark session
spark = SparkSession.builder \
    .appName("Agg Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Apply different aggregations
df2 = df.groupBy("department_id").agg(
    count("employee_id").alias("employee_count"),
    sum("salary").alias("total_salary"),
    avg("salary").alias("average_salary"),
    max("salary").alias("maximum_salary"),
    min("salary").alias("minimum_salary")
)

# Display data
print("Department Statistics:")
df2.show()


# Count distinct departments
df3 = df.groupBy().agg(
    countDistinct("department_id").alias("unique_departments")
)

print("Count Distinct:")
df3.show()

# First salary in each department
df4 = df.groupBy("department_id").agg(
    first("salary").alias("first_salary")
)

print("First:")
df4.show()

# Last salary in each department
df5 = df.groupBy("department_id").agg(
    last("salary").alias("last_salary")
)

print("Last:")
df5.show()

# Collect employee names
df6 = df.groupBy("department_id").agg(
    collect_list("name").alias("employee_names")
)

print("Collect List:")
df6.show(truncate=False)

# Collect unique employee names
df7 = df.groupBy("department_id").agg(
    collect_set("name").alias("unique_employee_names")
)

print("Collect Set:")
df7.show(truncate=False)


# Stop Spark
spark.stop()