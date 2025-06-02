from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.weather import get_weather_forecast

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    try:
        forecast = await get_weather_forecast(city_name=city)
        print(forecast)
        return templates.TemplateResponse(
            "index.html", {"request": request, "city": city, "forecast": forecast}
        )
    except Exception as e:
        print(e)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "city": city, "forecast": None, "error": str(e)},
        )
