from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    abs,
    round,
    ceil,
    floor,
    sqrt,
    pow,
    greatest,
    least
)

# Create Spark session
spark = SparkSession.builder \
    .appName("Numeric Functions Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Absolute value
df2 = df.withColumn(
    "absolute_salary",
    abs("salary")
)

print("Absolute:")
df2.show()

# Round
df3 = df.withColumn(
    "rounded_salary",
    round("salary", -3)
)

print("Round:")
df3.show()

# Ceiling
df4 = df.withColumn(
    "ceil_salary",
    ceil("salary")
)

print("Ceil:")
df4.show()

# Floor
df5 = df.withColumn(
    "floor_salary",
    floor("salary")
)

print("Floor:")
df5.show()

# Square root
df6 = df.withColumn(
    "salary_sqrt",
    sqrt("salary")
)

print("Square Root:")
df6.show()

# Power
df7 = df.withColumn(
    "salary_power",
    pow("salary", 2)
)

print("Power:")
df7.show()

# Greatest value
df8 = df.withColumn(
    "greatest_value",
    greatest("salary", "department_id")
)

print("Greatest:")
df8.show()

# Least value
df9 = df.withColumn(
    "least_value",
    least("salary", "department_id")
)

print("Least:")
df9.show()

# Stop Spark
spark.stop()