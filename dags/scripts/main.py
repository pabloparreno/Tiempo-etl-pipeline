from .extract import extract_weather_data
from .transform import transform_weather_data
from .load_bq import load_to_bigquery

def run_pipeline():

    print("🚀 Starting ETL pipeline...")

    raw = extract_weather_data()
    print("✅ Extract done")

    df = transform_weather_data(raw)
    print("✅ Transform done")

    load_to_bigquery(df)
    print("✅ Load done")

    print("🎉 Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()