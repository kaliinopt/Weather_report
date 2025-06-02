# Weather Forecast Application

FastAPI-приложение для получения прогноза погоды через Open-Meteo API

## ⚙️ Технологии

- Python 3.10+
- FastAPI (веб-фреймворк)
- Jinja2 (шаблонизация)
- HTTPX (HTTP-клиент)
- Open-Meteo API (данные о погоде)

## 🚀 Быстрый старт

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. Создайте и активируйте виртуальное окружение:
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
### Запуск 

1. Запустите приложение:
    ```bash
    uvicorn app.main:app --reload
    ```
2. Откройте в браузере:
    ```
    http://localhost:8000
    ```

### 