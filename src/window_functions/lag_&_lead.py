from pyspark.sql import SparkSession
from pyspark.sql.functions import lag, lead
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("Lag Lead Practice") \
    .getOrCreate()

# Read CSV
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("src/utils/employees.csv")

# Create window
window = Window \
    .partitionBy("department_id") \
    .orderBy("employee_id")

# Apply lag
df2 = df.withColumn(
    "previous_salary",
    lag("salary", 1).over(window)
)

print("Lag:")
df2.show()

# Apply lead
df3 = df.withColumn(
    "next_salary",
    lead("salary", 1).over(window)
)

print("Lead:")
df3.show()

# Stop Spark
spark.stop()