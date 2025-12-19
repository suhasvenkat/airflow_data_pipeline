from __future__ import annotations

import pandas as pd
from typing import Any

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

# ----------------------------------------------------
# CONFIG
# ----------------------------------------------------
POSTGRES_CONN_ID = "postgres_default"

FILE_ONE_PATH = "/usr/local/airflow/include/data/building_metadata.csv"
FILE_TWO_PATH = "/usr/local/airflow/include/data/wther.csv"

TABLE_ONE_NAME = "building"
TABLE_TWO_NAME = "weather"


def load_csv_to_postgres(file_path: str, table_name: str, **kwargs: Any) -> None:
    print(f"Starting ETL for {file_path}")

    # -------------------- EXTRACT --------------------
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows")

    # -------------------- TRANSFORM ------------------
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    if "price" in df.columns:
        df["price"] = df["price"].fillna(0).astype(float)

    if "quantity" in df.columns:
        df["quantity"] = df["quantity"].fillna(0).astype(int)

    if "id" in df.columns:
        df.dropna(subset=["id"], inplace=True)

    df.drop_duplicates(inplace=True)

    if {"price", "quantity"}.issubset(df.columns):
        df["tax_amount"] = df["price"] * df["quantity"] * 0.05

    print(f"After transform: {df.shape}")

    # -------------------- LOAD -----------------------
    pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
    engine = pg_hook.get_sqlalchemy_engine()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded data into {table_name}")


with DAG(
    dag_id="csv_to_postgres_etl",
    start_date=datetime(2025, 12, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "csv", "postgres"],
) as dag:

    load_building = PythonOperator(
        task_id="load_building_data",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "file_path": FILE_ONE_PATH,
            "table_name": TABLE_ONE_NAME,
        },
    )

    load_weather = PythonOperator(
        task_id="load_weather_data",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "file_path": FILE_TWO_PATH,
            "table_name": TABLE_TWO_NAME,
        },
    )

    # Parallel execution
    [load_building, load_weather]
