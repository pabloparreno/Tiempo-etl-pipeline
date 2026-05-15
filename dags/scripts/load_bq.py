from google.cloud import bigquery
from google.api_core.exceptions import NotFound
import pandas as pd


def load_to_bigquery(df):

    client = bigquery.Client()

    project_id = client.project
    dataset_id = "Clima_data"
    table_id = "Clima_diario"

    dataset_ref = f"{project_id}.{dataset_id}"
    table_ref = f"{dataset_ref}.{table_id}"

    # =========================================================
    # CREAR DATASET SI NO EXISTE
    # =========================================================

    try:
        client.get_dataset(dataset_ref)
        print(f"✅ Dataset existe: {dataset_ref}")

    except NotFound:

        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "EU"

        client.create_dataset(dataset)

        print(f"✅ Dataset creado: {dataset_ref}")

    # =========================================================
    # COMPROBAR SI LA TABLA EXISTE
    # =========================================================

    table_exists = True

    try:
        table = client.get_table(table_ref)

    except NotFound:
        table_exists = False

    # =========================================================
    # SI NO EXISTE → CREAR TABLA AUTOMÁTICAMENTE
    # =========================================================

    if not table_exists:

        print(f"⚠️ Tabla no existe. Creando: {table_ref}")

        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            write_disposition="WRITE_APPEND"
        )

        job = client.load_table_from_dataframe(
            df,
            table_ref,
            job_config=job_config
        )

        job.result()

        print(f"✅ Tabla creada automáticamente: {table_ref}")

        return

    # =========================================================
    # TABLA EXISTE → INSERT NORMAL
    # =========================================================

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