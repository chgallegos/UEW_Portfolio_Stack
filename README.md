# UEW_Portfolio_Stack

---

## Purpose

This repository demonstrates my ability to design and implement **ETL pipelines**, **workflow orchestration** using **Apache Airflow**, and **data integration workflows** while ensuring data quality. It highlights my technical expertise in handling data systems and my understanding of scalable, efficient workflows.

---

## Key Features

### 1. ETL Pipeline
- **Description**: A complete ETL pipeline that extracts data from an API, transforms it using `pandas`, validates the data, and loads it into a PostgreSQL database.
- **Technologies**: Python, SQLAlchemy, PostgreSQL, pandas.
- **Location**: See the [Python Example 1](Python/ETL_Example_1/etl_pipeline.py) and [Python Example 2](Python/ETL_Example_2/PyCitySchools_Challenge.ipynb) file for details.

### 2. Apache Airflow DAGs
- **Description**: Workflow orchestration using Airflow to automate, schedule, and monitor ETL processes.
  - `simple_etl_dag.py`: A basic ETL workflow orchestrated with Airflow.
  - `complex_etl_dag.py`: Demonstrates advanced capabilities with task groups, branching, and dynamic task generation.
- **Technologies**: Apache Airflow, Python.
- **Location**: See the [Airflow](Airflow/Dags/) directory.

### 3. SQL Queries
- **Description**: SQL scripts for querying relational databases, including data aggregation and analysis.
- **Technologies**: SQL, PostgreSQL.
- **Location**: See the [SQL](/SQL/Example%201/Queries.sql) example.

### 4. Data Validation
- **Description**: Scripts for ensuring data quality, validating schema conformity, and handling missing values.
- **Technologies**: Python.
- **Location**: See the [Data Validation](Python/Data_Validation_Example_1/Validation.py) example.

### 5. Exploratory Data Analysis (EDA)
- **Description**: Jupyter Notebook showcasing data visualization and insights generation.
- **Technologies**: Python, pandas, matplotlib, Jupyter Notebook.
- **Location**: See the [Exploratory Data Analysis](Python/EDA_Example_1/EDA.py) directory.

---

## Running Airflow DAGs

1. **Install Airflow**:
   Follow the [official installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) or use the requirements file:
   ```bash
   pip install apache-airflow
