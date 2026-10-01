# PySpark_Practice

This repository contains my PySpark practice and learning exercises, covering PySpark fundamentals, DataFrame operations, transformations, joins, aggregations, window functions, array functions, nested data, UDFs, Slowly Changing Dimensions (SCD), and other PySpark concepts.

## Topics Covered

### PySpark Basics

- Creating a SparkSession
- Creating DataFrames
- `show()`
- `printSchema()`
- `select()`
- `filter()`
- `where()`
- `withColumn()`
- `withColumnRenamed()`
- `drop()`
- `sort()`
- `distinct()`
- `dropDuplicates()`
- `limit()`
- `count()`

### Reading and Writing Data

- Reading CSV
- Reading JSON
- Reading Parquet
- Writing CSV
- Writing JSON
- Writing Parquet
- Explicit Schema
- Schema Definition
- Data Types

### Transformations

- `select()`
- `filter()`
- `where()`
- `withColumn()`
- `withColumnRenamed()`
- `when()`
- `drop()`
- `distinct()`
- `dropDuplicates()`
- `sort()`
- `orderBy()`
- `limit()`
- `fillna()`
- `dropna()`
- `sample()`
- `randomSplit()`

### String Functions

- `lower()`
- `upper()`
- `trim()`
- `ltrim()`
- `rtrim()`
- `length()`
- `concat()`
- `concat_ws()`
- `substring()`
- `split()`
- `regexp_replace()`
- `regexp_extract()`

### Numeric Functions

- `abs()`
- `round()`
- `ceil()`
- `floor()`
- `sqrt()`
- `pow()`
- `greatest()`
- `least()`

### Aggregation Functions

- `count()`
- `sum()`
- `avg()`
- `max()`
- `min()`
- `countDistinct()`
- `first()`
- `last()`
- `collect_list()`
- `collect_set()`
- Conditional Aggregation

### GroupBy

- `groupBy()`
- `agg()`
- Grouping and Aggregation
- Multiple Aggregations

### Joins

- Inner Join
- Left Join
- Right Join
- Full Join
- Left Semi Join
- Left Anti Join
- Cross Join
- Multiple-column Joins
- Advanced Join Concepts
- Broadcast Join
- Shuffle Join

### Window Functions

- `row_number()`
- Running Total
- `rank()`
- `dense_rank()`
- `lag()`
- `lead()`
- Window specification

### Array Functions

- `array()`
- `array_contains()`
- `array_size()`
- `array_position()`
- `array_remove()`
- `array_distinct()`
- `flatten()`
- `array_sort()`
- `element_at()`
- `array_intersect()`
- `array_union()`
- `array_except()`
- `array_join()`
- `array_insert()`
- `array_compact()`

### Explode Functions

- `explode()`
- `explode_outer()`
- `posexplode()`
- `posexplode_outer()`

### Nested Data

- Nested DataFrames
- Array columns
- Struct columns
- Nested JSON data
- `from_json()`
- Accessing nested fields
- Exploding nested arrays

### User Defined Functions

- Creating Python functions
- Creating PySpark UDFs
- Defining return types
- Applying UDFs to DataFrames
- Understanding UDF limitations
- Using built-in Spark functions instead of UDFs where possible

### Slowly Changing Dimensions

- SCD Type 1
- SCD Type 2
- SCD Type 3

### Loads

- Full Load
- Incremental Load
- Snapshot Load
  - Full Snapshot
  - Incremental Snapshot
  - Rolling Snapshot

### DataFrame Operations

- Creating DataFrames
- DataFrame transformations
- DataFrame actions
- Handling null values
- Sorting and filtering
- Removing duplicates
- Combining DataFrames

### Performance Concepts

- Caching
- `cache()`
- `unpersist()`
- Broadcast Join
- Shuffle Join

---

## Project Structure

```text
PySpark_Practice/
│
├── src/
│   │
│   ├── aggregations/
│   │   ├── agg_functions.py
│   │   └── groupby.py
│   │
│   ├── array_functions/
│   │   ├── array_functions.py
│   │   └── explode.py
│   │
│   ├── basic_syntax/
│   │   └── basic_syntax.py
│   │
│   ├── explicit_schema/
│   │   └── explicit_schema.py
│   │
│   ├── joins/
│   │   ├── anti_join.py
│   │   ├── full_join.py
│   │   ├── inner_join.py
│   │   ├── left_join.py
│   │   ├── right_join.py
│   │   └── semi_join.py
│   │
│   ├── nested_data/
│   │   ├── nested_csv.py
│   │   └── nested_json.py
│   │
│   ├── numeric_functions/
│   │   ├── numeric_functions.py
│   │   └── user_defined_functions.py
│   │
│   ├── read_write/
│   │   ├── csv_practice.py
│   │   ├── json_practice.py
│   │   └── parquet_practice.py
│   │
│   ├── scd/
│   │   ├── type_1.py
│   │   ├── type_2.py
│   │   └── type_3.py
│   │
│   ├── string_functions/
│   │   └── string_functions.py
│   │
│   ├── transformations/
│   │   ├── filter.py
│   │   ├── select.py
│   │   ├── unions().py
│   │   ├── useful_transformations.py
│   │   ├── when.py
│   │   └── with_column.py
│   │
│   ├── utils/
│   │   ├── department.csv
│   │   ├── department.json
│   │   ├── employees.csv
│   │   └── employees.json
│   │
│   └── window_functions/
│       ├── lag_&_lead.py
│       ├── rank_&_dense_rank.py
│       ├── row_number.py
│       └── running_total.py
│
└── README.md
