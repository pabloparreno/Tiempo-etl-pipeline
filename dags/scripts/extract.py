from dotenv import load_dotenv
import os
import requests

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY")

print("API KEY LOADED:", API_KEY)  # DEBUG (quitar en producción)

def extract_weather_data():

    # Validación básica de configuración
    if not API_KEY:
        raise ValueError("❌ API key no cargada desde .env")

    if not CITY:
        raise ValueError("❌ CITY no definida en .env")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    print("STATUS CODE:", response.status_code)  # DEBUG

    # Lanza error si la API falla
    response.raise_for_status()

    data = response.json()

    return data


# Permite probar el script solo
if __name__ == "__main__":
    result = extract_weather_data()
    print(result)