import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from main import app

@pytest.mark.asyncio
@pytest_asyncio.fixture(scope='function')
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as client:
        yield client

@pytest.fixture
def mock_forecast_error():
    raise Exception("Сервис open-meteo.com не доступен")


@pytest.fixture
def mock_forecast_success():
    return {
        "forecast": [
{'time': '04.06.2025 16:00', 'temperature': 17.9, 'pressure': 1007.1, 'wind_speed': 11.2, 'clouds': 100, 'humidity': 58}, 
{'time': '04.06.2025 17:00', 'temperature': 17.8, 'pressure': 1007.4, 'wind_speed': 9.6, 'clouds': 100, 'humidity': 60}, 
{'time': '04.06.2025 18:00', 'temperature': 17.8, 'pressure': 1007.7, 'wind_speed': 10.1, 'clouds': 100, 'humidity': 60}, 
{'time': '04.06.2025 19:00', 'temperature': 17.3, 'pressure': 1008.0, 'wind_speed': 6.9, 'clouds': 100, 'humidity': 64}
        ]
    }
