from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("Row Number Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Create window
window = Window \
    .partitionBy("department_id") \
    .orderBy(df.salary.desc())

# Apply row_number
df2 = df.withColumn(
    "row_number",
    row_number().over(window)
)

# Display data
print("Row Number:")
df2.show()

# Stop Spark
spark.stop()