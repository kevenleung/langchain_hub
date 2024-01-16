import os
import requests

from typing import Type, Any
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

### 使用该api可前往https://api.openweathermap.org注册获得api_key

class WeatherInput(BaseModel):
    location: str = Field(description="the location need to check the weather")


class Weather(BaseTool):
    name = "weather"
    description = "Use for searching weather at a specific location"
    args_schema: Type[BaseModel] = WeatherInput

    def __init__(self):
        super().__init__()

    def _run(self, location: str) -> dict[str, Any]:
        api_key = os.environ["WEATHER_API_KEY"]
        # 此处根据经纬度查询天气信息，如果需要更加城市查询，需要查找相应的参数
        lon = 113.0
        lat = 23.0
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}&lang=zh_cn"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            wind_info = data['wind']
            main_info = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main_info["temp"]
            hum = main_info['humidity']
            pressure = main_info['pressure']
            temp_diff = main_info['temp_max'] - main_info['temp_min']
            wind_deg = wind_info['deg']
            if wind_deg <= 5 and wind_deg >= 355:
                wind_deg = '西风'
            elif wind_deg < 85 and wind_deg > 5:
                wind_deg = '西南风'
            elif wind_deg >= 85 and wind_deg <= 95:
                wind_deg = '南风'
            elif wind_deg > 95 and wind_deg < 175:
                wind_deg = '东南风'
            elif wind_deg >= 175 and wind_deg <= 185:
                wind_deg = '东风'
            elif wind_deg > 185 and wind_deg < 265:
                wind_deg = '东北风'
            elif wind_deg >= 265 and wind_deg <= 275:
                wind_deg = '北风'
            elif wind_deg > 275 and wind_deg < 355:
                wind_deg = '西北风'
            wind_speed = wind_info['speed']
            if temp_diff > 10:
                desc = f"{weather_desc} 气温{temp}°C 温差{temp_diff}°C 湿度{hum}% 大气压{pressure}hpa {wind_deg} 风速{wind_speed}"
            else:
                desc = f"{weather_desc} 气温{temp}°C 湿度{hum}% 大气压{pressure}hpa {wind_deg} 风速{wind_speed}"
            
            weather = {
                "temperature": temp,
                "description": desc,
            }
            return weather
        else:
            raise Exception(
                f"Failed to retrieve weather: {response.status_code}")
