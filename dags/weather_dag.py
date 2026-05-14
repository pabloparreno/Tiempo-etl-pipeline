from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.main import run_pipeline   # 👈 ESTO ES OBLIGATORIO

import sys
import os

default_args = {
    "owner": "Pablo",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "bigquery", "weather"]
) as dag:

    run_etl = PythonOperator(
        task_id="run_weather_pipeline",
        python_callable=run_pipeline
    )

    run_etl