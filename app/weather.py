from httpx import AsyncClient
from datetime import datetime


async def get_weather_forecast(city_name: str):
    async with AsyncClient() as client:

        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {"name": city_name, "count": 1, "language": "ru"}
        try:
            geo_resp = await client.get(geo_url, params=geo_params)
            geo_data = geo_resp.json()
        except Exception as e:
            print(e)
            raise Exception("Сервис open-meteo.com не доступен")

        if not geo_data.get("results"):
            return {"error": "Город не найден"}

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,pressure_msl,windspeed_10m,relativehumidity_2m,cloudcover",
            "forecast_days": 3,
            "timezone": "auto",
            "wind_speed_unit": "kmh",
        }
        try:

            resp = await client.get(url=url, params=params)
            data = resp.json()
        except Exception as e:
            print(e)
            raise Exception("Сервис open-meteo.com не доступен")

        time = data.get("hourly", {}).get("time", [])
        temps = data.get("hourly", {}).get("temperature_2m", [])
        wind_speeds = data.get("hourly", {}).get("windspeed_10m", [])
        pressures = data.get("hourly", {}).get("pressure_msl", [])
        clouds = data.get("hourly", {}).get("cloudcover", [])
        humidity = data.get("hourly", {}).get("relativehumidity_2m", [])

        print(data)
        forecast = []
        for i in range(len(time)):
            dt = datetime.fromisoformat(time[i])
            formated_time = dt.strftime("%d.%m.%Y %H:%M")
            forecast.append(
                {
                    "time": formated_time,
                    "temperature": temps[i],
                    "pressure": pressures[i],
                    "wind_speed": wind_speeds[i],
                    "clouds": clouds[i],
                    "humidity": humidity[i],
                }
            )
        return {"forecast": forecast}
