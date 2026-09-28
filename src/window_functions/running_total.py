from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("Running Total Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Create window
window = Window \
    .partitionBy("department_id") \
    .orderBy("employee_id") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Calculate running total
df2 = df.withColumn(
    "running_total",
    sum("salary").over(window)
)

# Display data
print("Running Total:")
df2.show()

# Stop Spark
spark.stop()