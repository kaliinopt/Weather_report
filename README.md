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

### Запуск через докер


1. Соберите Docker-образ:
   ```bash
   docker build -t weather-app .
   ```

2. Запустите контейнер:

    ```bash
    docker run -p 8000:8000 --name weather-container weather-app
    ```
3. Приложение будет доступно по адресу:
    ```
    http://localhost:8000
    ```