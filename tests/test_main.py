import pytest
from httpx import AsyncClient
from unittest.mock import patch

@pytest.mark.asyncio
async def test_home_page(client: AsyncClient):
    response = await client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

@pytest.mark.asyncio
async def test_get_weather_success(client, mock_forecast_success):
    with patch("main.get_weather_forecast", return_value=mock_forecast_success):
        response = await client.post("/", data={"city": "Moscow"})
    
    assert response.status_code == 200
    assert "Moscow" in response.text
    assert "17.9" in response.text 