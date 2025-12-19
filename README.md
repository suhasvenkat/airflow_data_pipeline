Airflow Data Pipeline – CSV to PostgreSQL
📌 Project Overview

This project is a beginner-friendly Apache Airflow ETL pipeline that reads data from CSV files, performs basic data cleaning and transformation using Python, and loads the processed data into a PostgreSQL database.

The goal of this project is to understand how Airflow, Python, Docker, and PostgreSQL work together in a real data engineering pipeline.

🛠️ Tech Stack

Apache Airflow (Astro Runtime)

Python (Pandas, SQLAlchemy)

PostgreSQL

Docker

pgAdmin

📂 Project Structure
airflow_data_pipeline/
├── dags/                     # Airflow DAGs
│   └── load_excel_to_postgres.py
├── include/
│   └── data/
│       ├── building_metadata.csv
│       └── wther.csv
├── Dockerfile
├── requirements.txt
├── packages.txt
├── airflow_settings.yaml
├── config.yaml
└── README.md
🔄 Pipeline Workflow

Extract

Read CSV files from include/data

Transform

Standardize column names

Handle NULL values

Remove duplicates

Perform basic feature engineering

Load

Load cleaned data into PostgreSQL tables:

building

weather

Orchestration

Managed and scheduled using Apache Airflow

▶️ How to Run the Project
1️⃣ Start Airflow
astro dev start
2️⃣ Open Airflow UI
http://localhost:8080
3️⃣ Trigger the DAG

DAG name: csv_to_postgres_etl

Trigger manually from the Airflow UI

🧪 Verify Output

You can verify the tables using pgAdmin or psql:

SELECT COUNT(*) FROM building;
SELECT COUNT(*) FROM weather;
✅ Features Implemented

Dockerized Airflow environment

CSV to PostgreSQL ETL pipeline

Data cleaning and transformation using Pandas

PostgreSQL integration using Airflow hooks

Manual DAG execution

🚀 Future Improvements

Incremental data loading

TaskFlow API implementation

Data quality checks

Logging and monitoring

Error handling and retries

👤 Author

Suhas Venkat

Beginner Data Engineer | Learning Apache Airflow & Data Engineering