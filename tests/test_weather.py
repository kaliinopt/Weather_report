import pytest
from unittest.mock import patch
from app.weather import get_weather_forecast
import httpx

cities = [ 
    'Вологда', 
    'Чебоксары', 
    'Тольятти', 
    'Москва', 
    'Бремен', 
    'Санкт-Петербург', 
    'Новороссийск', 
    'Челябинск', 
    'Вологда', 
    'Новосибирск', 
    'Челябинск', 
    'Санкт-Петербург', 
    'Москва', 
    'Новосибирск' 
] 



@pytest.mark.asyncio
@pytest.mark.parametrize("cityes", cities)
async def test_get_weather_forecast(cityes):
    result = await get_weather_forecast(cityes)

    assert "forecast" in result
    assert len(result["forecast"]) == 72


@pytest.mark.asyncio
async def test_city_not_found():
    result = await get_weather_forecast("some_wrong_city")

    assert result == {"error": "Город не найден"}


@pytest.mark.asyncio
async def test_api_unavailable():
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.side_effect = httpx.RequestError("API недоступен")
        with pytest.raises(Exception, match="Сервис open-meteo.com не доступен"):
            await get_weather_forecast("Moscow")
