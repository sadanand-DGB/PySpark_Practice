from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder \
    .appName("UDF Practice") \
    .getOrCreate()

data = [
    (1, 100),
    (2, 200),
    (3, 300)
]

df = spark.createDataFrame(data, ["id", "salary"])


def add_bonus(salary):
    return salary + 5000


bonus_udf = udf(add_bonus, IntegerType())

df2 = df.withColumn(
    "salary_with_bonus",
    bonus_udf(df.salary)
)

df2.show()

spark.stop()