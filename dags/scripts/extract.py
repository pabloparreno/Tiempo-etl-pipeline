import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = os.getenv("CITIES", "").split(",")

BASE_URL = "https://api.openweathermap.org/data/2.5"


def extract_current_weather(city):
    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    r = requests.get(url)

    if r.status_code != 200:
        print(f"❌ Error API for {city}: {r.text}")
        return None

    return r.json()


def extract_forecast(city):

    url = (
        f"{BASE_URL}/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    r = requests.get(url)
    r.raise_for_status()

    return r.json()


def extract_air_pollution(lat, lon):

    url = (
        f"{BASE_URL}/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    r = requests.get(url)
    r.raise_for_status()

    return r.json()


def extract_all():

    if not API_KEY:
        raise ValueError("❌ API key missing")

    if not CITIES:
        raise ValueError("❌ No cities configured")

    all_data = []

    for city in CITIES:

        city = city.strip()

        print(f"🌍 Extracting data for {city}")

        current = extract_current_weather(city)

        coords = current["coord"]

        forecast = extract_forecast(city)

        pollution = extract_air_pollution(
            coords["lat"],
            coords["lon"]
        )

        all_data.append({
            "current": current,
            "forecast": forecast,
            "air_quality": pollution
        })

    return all_data