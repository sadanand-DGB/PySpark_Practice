from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    array,
    array_contains,
    array_size,
    array_position,
    array_remove,
    array_distinct,
    flatten,
    array_sort,
    element_at,
    array_intersect,
    array_union,
    array_except,
    array_join,
    array_insert,
    array_compact
)

spark = SparkSession.builder \
    .appName("Array Functions") \
    .getOrCreate()

data = [
    (1, "Rahul", ["Python", "SQL", "Python"], ["SQL", "Spark"]),
    (2, "Amit", ["Java", "SQL", None], ["SQL", "Java"]),
    (3, "Neha", ["Python", "Spark", "Python"], ["Java", "Spark"])
]

df = spark.createDataFrame(
    data,
    ["id", "name", "skills", "other_skills"]
)

# array
df2 = df.withColumn(
    "all_skills",
    array("skills", "other_skills")
)

# array_contains
df3 = df.withColumn(
    "has_python",
    array_contains("skills", "Python")
)

# array_size
df4 = df.withColumn(
    "skill_count",
    array_size("skills")
)

# array_position
df5 = df.withColumn(
    "python_position",
    array_position("skills", "Python")
)

# array_remove
df6 = df.withColumn(
    "without_python",
    array_remove("skills", "Python")
)

# array_distinct
df7 = df.withColumn(
    "unique_skills",
    array_distinct("skills")
)

# flatten
df8 = df2.withColumn(
    "flattened_skills",
    flatten("all_skills")
)

# array_sort
df9 = df.withColumn(
    "sorted_skills",
    array_sort("skills")
)

# element_at
df10 = df.withColumn(
    "first_skill",
    element_at("skills", 1)
)

# array_intersect
df11 = df.withColumn(
    "common_skills",
    array_intersect("skills", "other_skills")
)

# array_union
df12 = df.withColumn(
    "combined_skills",
    array_union("skills", "other_skills")
)

# array_except
df13 = df.withColumn(
    "unique_to_skills",
    array_except("skills", "other_skills")
)

# array_join
df14 = df.withColumn(
    "skills_string",
    array_join("skills", ", ")
)

# array_insert
df15 = df.withColumn(
    "inserted_skill",
    array_insert("skills", 2, "PySpark")
)

# array_compact
df16 = df.withColumn(
    "without_null",
    array_compact("skills")
)

df16.show(truncate=False)

spark.stop()