from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType
)

spark = SparkSession.builder \
    .appName("Nested JSON") \
    .getOrCreate()

# Create JSON string data
data = [
    (1, '{"city":"Delhi","state":"Delhi"}'),
    (2, '{"city":"Mumbai","state":"Maharashtra"}'),
    (3, '{"city":"Bengaluru","state":"Karnataka"}')
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["id", "address"]
)

df.show(truncate=False)

# Define nested schema
address_schema = StructType([
    StructField("city", StringType()),
    StructField("state", StringType())
])

# Convert JSON string into struct
df2 = df.withColumn(
    "address_data",
    from_json("address", address_schema)
)

df2.printSchema()
df2.show(truncate=False)

# Access nested fields
df3 = df2.select(
    "id",
    "address_data.city",
    "address_data.state"
)

df3.show()

spark.stop()