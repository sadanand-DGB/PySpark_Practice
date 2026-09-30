from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Other Transformations Practice") \
    .getOrCreate()

data = [
    (1, "Rahul", 50000, 101),
    (2, "Amit", 60000, 102),
    (3, "Neha", 45000, 101),
    (4, "Priya", 70000, 103),
    (5, "Aman", None, 102)
]

df = spark.createDataFrame(
    data,
    ["employee_id", "name", "salary", "department_id"]
)


# where
df2 = df.where(
    df.salary > 50000
)

print("Where:")
df2.show()


# like
df3 = df.filter(
    df.name.like("A%")
)

print("Like:")
df3.show()


# withColumnRenamed
df4 = df.withColumnRenamed(
    "name",
    "employee_name"
)

print("With Column Renamed:")
df4.show()


# drop
df5 = df.drop(
    "salary"
)

print("Drop:")
df5.show()


# distinct
df6 = df.distinct()

print("Distinct:")
df6.show()


# dropDuplicates
df7 = df.dropDuplicates(
    ["department_id"]
)

print("Drop Duplicates:")
df7.show()


# sort
df8 = df.sort(
    "department_id"
)

print("Sort:")
df8.show()


# orderBy descending
df9 = df.orderBy(
    df.salary.desc()
)

print("Order By:")
df9.show()


# limit
df10 = df.limit(3)

print("Limit:")
df10.show()


# fillna
df11 = df.fillna({
    "salary": 0
})

print("Fill NA:")
df11.show()


# na.fill
df12 = df.na.fill({
    "salary": 0
})

print("NA Fill:")
df12.show()


# dropna
df13 = df.dropna()

print("Drop NA:")
df13.show()


# dropna for specific column
df14 = df.dropna(
    subset=["salary"]
)

print("Drop NA from Salary:")
df14.show()


# sample
df15 = df.sample(
    fraction=0.5,
    seed=42
)

print("Sample:")
df15.show()


# randomSplit
df16, df17 = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

print("Random Split - 80%:")
df16.show()

print("Random Split - 20%:")
df17.show()


# pivot
pivot_data = [
    ("IT", 2025, 50000),
    ("IT", 2026, 60000),
    ("HR", 2025, 40000),
    ("HR", 2026, 45000)
]

pivot_df = spark.createDataFrame(
    pivot_data,
    ["department", "year", "salary"]
)

df18 = pivot_df.groupBy(
    "department"
).pivot(
    "year"
).sum(
    "salary"
)

print("Pivot:")
df18.show()


# unpivot
unpivot_data = [
    ("Rahul", 50000, 60000),
    ("Amit", 55000, 65000)
]

unpivot_df = spark.createDataFrame(
    unpivot_data,
    ["name", "2025", "2026"]
)

df19 = unpivot_df.unpivot(
    "name",
    ["2025", "2026"],
    "year",
    "salary"
)

print("Unpivot:")
df19.show()


spark.stop()