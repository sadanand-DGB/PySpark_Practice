from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    lower,
    upper,
    trim,
    ltrim,
    rtrim,
    length,
    concat,
    concat_ws,
    substring,
    split,
    regexp_replace,
    regexp_extract
)

# Create Spark session
spark = SparkSession.builder \
    .appName("String Functions Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Lowercase
df2 = df.withColumn(
    "lower_name",
    lower("name")
)

print("Lower:")
df2.show()

# Uppercase
df3 = df.withColumn(
    "upper_name",
    upper("name")
)

print("Upper:")
df3.show()

# Trim
df4 = df.withColumn(
    "trimmed_name",
    trim("name")
)

print("Trim:")
df4.show()

# Left trim
df5 = df.withColumn(
    "left_trimmed_name",
    ltrim("name")
)

print("Left Trim:")
df5.show()

# Right trim
df6 = df.withColumn(
    "right_trimmed_name",
    rtrim("name")
)

print("Right Trim:")
df6.show()

# Length
df7 = df.withColumn(
    "name_length",
    length("name")
)

print("Length:")
df7.show()

# Concatenate
df8 = df.withColumn(
    "employee_info",
    concat("name", "department_id")
)

print("Concat:")
df8.show()

# Concatenate with separator
df9 = df.withColumn(
    "employee_info",
    concat_ws("-", "name", "department_id")
)

print("Concat WS:")
df9.show()

# Substring
df10 = df.withColumn(
    "short_name",
    substring("name", 1, 3)
)

print("Substring:")
df10.show()

# Split
df11 = df.withColumn(
    "name_parts",
    split("name", "")
)

print("Split:")
df11.show(truncate=False)

# Replace text using regular expression
df12 = df.withColumn(
    "clean_name",
    regexp_replace("name", "a", "@")
)

print("Regex Replace:")
df12.show()

# Extract text using regular expression
df13 = df.withColumn(
    "first_letter",
    regexp_extract("name", "^.", 0)
)

print("Regex Extract:")
df13.show()

# Stop Spark
spark.stop()