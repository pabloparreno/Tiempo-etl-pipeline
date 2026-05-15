from .extract import extract_all
from .transform import transformar_datos_clima
from .load_bq import load_to_bigquery

import pandas as pd


def run_pipeline():

    print("🚀 Starting ETL pipeline...")

    raw_data = extract_all()

    print("✅ Extract done")

    all_dataframes = []

    for city_data in raw_data:

        ciudad = city_data["current"]["name"]

        df = transformar_datos_clima(
            city_data["current"],
            ciudad_input=ciudad
        )

        if df is not None and not df.empty:
            all_dataframes.append(df)

    if not all_dataframes:
        raise ValueError("❌ No valid data to load into BigQuery")

    final_df = pd.concat(all_dataframes, ignore_index=True)

    print("✅ Transform done")

    load_to_bigquery(final_df)

    print("✅ Load done")
    print("🎉 Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()