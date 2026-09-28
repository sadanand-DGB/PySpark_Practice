from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Create Spark session
spark = SparkSession.builder\
       .appName("When Practice") \
       .getOrCreate()

# Read CSV
df = spark.read \
     .option("header", True) \
     .option("inferSchema", True) \
      .csv("src/utils/employees.csv")

# Add a new column based on conditions using when
df2 = df.withColumn("salary_category", 
                    when(df.salary > 50000, "High")
                   .when(df.salary > 30000, "Medium") 
                   .otherwise("Low")
                   )

# Display data
print("Employees Data with Salary Category:")
df2.show()

# Stop Spark
spark.stop()