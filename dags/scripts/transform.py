import pandas as pd
from datetime import datetime, timezone
import pytz


TRADUCCION_CLIMA = {
    "Clear": "Despejado",
    "Clouds": "Nublado",
    "Rain": "Lluvia",
    "Drizzle": "Llovizna",
    "Thunderstorm": "Tormenta",
    "Snow": "Nieve",
    "Mist": "Niebla",
    "Smoke": "Humo",
    "Haze": "Bruma",
    "Dust": "Polvo",
    "Fog": "Niebla",
}


def transformar_datos_clima(raw_data, ciudad_input=None):

    if not raw_data or not isinstance(raw_data, dict):
        return None

    main = raw_data.get("main") or {}
    weather = (raw_data.get("weather") or [{}])[0]
    sys = raw_data.get("sys") or {}
    ciudad = ciudad_input or raw_data.get("name")

    dt_raw = raw_data.get("dt")

    fecha_clima = (
        datetime.fromtimestamp(dt_raw, tz=timezone.utc)
        if isinstance(dt_raw, (int, float))
        else None
    )

    timezone_spain = pytz.timezone("Europe/Madrid")

    clima_main = weather.get("main")

    return pd.DataFrame([{
        "ciudad": ciudad,
        "pais": sys.get("country"),
        "temperatura": main.get("temp"),
        "sensacion_termica": main.get("feels_like"),
        "humedad": main.get("humidity"),
        "presion": main.get("pressure"),
        "clima_principal": TRADUCCION_CLIMA.get(clima_main, clima_main),
        "fecha_insercion": datetime.now(timezone_spain)
    }])