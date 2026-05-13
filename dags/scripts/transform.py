import pandas as pd

def transform_weather_data(raw_data):

    # Validación básica
    if not raw_data:
        raise ValueError("❌ No hay datos para transformar")

    transformed = {
        "city": raw_data.get("name"),
        "temp": raw_data["main"]["temp"],
        "feels_like": raw_data["main"]["feels_like"],
        "humidity": raw_data["main"]["humidity"],
        "weather_main": raw_data["weather"][0]["main"],
        "timestamp": raw_data["dt"]
    }

    df = pd.DataFrame([transformed])

    return df


# Test local
if __name__ == "__main__":
    sample = {
        "name": "Madrid",
        "main": {
            "temp": 20,
            "feels_like": 19,
            "humidity": 60
        },
        "weather": [{"main": "Clouds"}],
        "dt": 123456789
    }

    df = transform_weather_data(sample)
    print(df)