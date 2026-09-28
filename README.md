# PySpark_Practice

This repository contains my PySpark practice and learning exercises, covering PySpark fundamentals, DataFrame operations, joins, aggregations, window functions, and other PySpark II concepts.

## Topics Covered

### PySpark I

- Reading and writing CSV
- Reading and writing JSON
- Reading and writing Parquet
- `select()`
- `filter()`
- `withColumn()`
- `when()`
- Joins
  - Inner Join
  - Left Join
  - Right Join
  - Full Join
  - Left Semi Join
  - Left Anti Join
- `groupBy()`
- Aggregation functions
- Explicit schemas
- Pandas to PySpark
- Creating DataFrames

### PySpark II

#### Window Functions

- `row_number()`
- Running Total
- `rank()`
- `dense_rank()`
- `lag()`
- `lead()`

#### String Functions

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

#### Numeric Functions

- `abs()`
- `round()`
- `ceil()`
- `floor()`
- `sqrt()`
- `pow()`
- `greatest()`
- `least()`

#### Aggregation Functions

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

#### Join and Performance Practice

- Basic Joins
- Broadcast Join
- Shuffle Join
- Multiple-column joins
- Advanced join concepts

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
│   ├── numeric_functions/
│   │   └── numeric_functions.py
│   │
│   ├── read_write/
│   │   ├── csv_practice.py
│   │   ├── json_practice.py
│   │   └── parquet_practice.py
│   │
│   ├── string_functions/
│   │   └── string_functions.py
│   │
│   ├── transformations/
│   │   ├── filter.py
│   │   ├── select.py
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
├── test_spark.py
├── .gitignore
└── README.md