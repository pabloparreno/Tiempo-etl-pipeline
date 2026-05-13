from google.cloud import bigquery
import os

def load_to_bigquery(df):

    # Cliente BigQuery (usa credenciales del .env)
    client = bigquery.Client()

    # Configuración
    project_id = client.project
    dataset_id = "Clima_data"
    table_id = "daily_weather"

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    # Configuración del job de carga
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )

    # Subir DataFrame
    job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    job.result()  # esperar a que termine

    print(f"✅ Data cargada en {table_ref}")