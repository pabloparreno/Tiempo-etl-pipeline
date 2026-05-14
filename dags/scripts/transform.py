import pandas as pd
from datetime import datetime, timezone

def transform_weather_data(raw_data):

    if not raw_data or not isinstance(raw_data, dict):
        return None

    main = raw_data.get("main") or {}
    weather = (raw_data.get("weather") or [{}])[0]
    sys = raw_data.get("sys") or {}

    city = raw_data.get("name")

    dt_raw = raw_data.get("dt")

    weather_datetime = (
        datetime.fromtimestamp(dt_raw, tz=timezone.utc)
        if isinstance(dt_raw, (int, float))
        else None
    )

    return pd.DataFrame([{
        "city": city,
        "country": sys.get("country"),
        "temp": main.get("temp"),
        "feels_like": main.get("feels_like"),
        "humidity": main.get("humidity"),
        "pressure": main.get("pressure"),
        "weather_main": weather.get("main"),
        "weather_description": weather.get("description"),
        "ingestion_datetime": datetime.now(timezone.utc)
    }])