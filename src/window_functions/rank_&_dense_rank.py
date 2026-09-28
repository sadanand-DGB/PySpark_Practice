from pyspark.sql import SparkSession
from pyspark.sql.functions import rank, dense_rank
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("Rank Practice") \
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

# Apply rank
df2 = df.withColumn(
    "rank",
    rank().over(window)
)

print("Rank:")
df2.show()

# Apply dense rank
df3 = df.withColumn(
    "dense_rank",
    dense_rank().over(window)
)

print("Dense Rank:")
df3.show()

# Stop Spark
spark.stop()