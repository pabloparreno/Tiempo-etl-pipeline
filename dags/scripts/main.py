from .extract import extract_all
from .transform import transform_weather_data
from .load_bq import load_to_bigquery

import pandas as pd


def run_pipeline():

    print("🚀 Starting ETL pipeline...")

    raw_data = extract_all()

    print("✅ Extract done")

    all_dataframes = []

    for city_data in raw_data:

        df = transform_weather_data(city_data["current"])

        # 🔒 FIX: evitar None o DataFrames vacíos
        if df is not None and not df.empty:
            all_dataframes.append(df)

    # 🔒 FIX: evitar crash si todo falla
    if not all_dataframes:
        raise ValueError("❌ No valid data to load into BigQuery")

    final_df = pd.concat(all_dataframes, ignore_index=True)

    print("✅ Transform done")

    load_to_bigquery(final_df)

    print("✅ Load done")

    print("🎉 Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()