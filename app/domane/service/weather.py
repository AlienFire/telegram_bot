from abc import ABC, abstractmethod
import aiohttp
from app.core.config import settings


class CityWeatherClientInterface(ABC):
    @abstractmethod
    async def city_weather(self) -> str:
        """метод возвращает погоду в городе"""
        raise NotImplementedError()


class CityWeatherClient(CityWeatherClientInterface):

    city: str

    def __init__(self, city: str) -> None:
        """
        city:str - название города на русском языке с большой буквы

        city_weather = CityWeather(city="Петрозаводск")
        """
        self.city = city

    async def city_weather(self) -> str:
        """метод возвращает погоду в городе"""
        temperature = await self._get_temperature()
        return f'Сейчас в городе {self.city} {temperature} °C'

    async def _get_temperature(self):
        """Извлекает температуру"""
        weather_data = await self._request_weather()
        return str(round(weather_data['main']['temp']))

    async def _request_weather(self):
        """метод для запроса погоды"""
        url = await self._get_weather_url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception("get return error")
                return await response.json()

    async def _get_weather_url(self):
        """метод составления url для запроса погоды"""
        return (
            f'{settings.WEATHER_HOST}'
            f'?q={self.city}&units=metric&lang=ru&'
            f'appid={settings.WEATHER_APPID}'
        )
