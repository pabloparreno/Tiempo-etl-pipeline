from google.cloud import bigquery
import pandas as pd


def load_to_bigquery(df):

    client = bigquery.Client()

    project_id = client.project
    dataset_id = "Clima_data"
    table_id = "daily_weather"

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    table = client.get_table(table_ref)

    existing_columns = [field.name for field in table.schema]

    print("📦 Columnas existentes en BigQuery:")
    print(existing_columns)

    print("📦 Columnas del DataFrame:")
    print(df.columns.tolist())

    df = df[[col for col in df.columns if col in existing_columns]]

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )

    job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    job.result()

    print(f"✅ Data cargada en {table_ref}")