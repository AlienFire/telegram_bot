from app.bot import bot
from app.domane.service.weather import CityWeatherClient
from app.domane.service.volute import VoluteClient
import asyncio

async def get_weather():
    city = CityWeatherClient(city='Сегежа')
    weather = await city.city_weather()
    print(weather)

async def get_volute():
    volute = VoluteClient(volute_data='USD')
    rate = await volute.actual_course()
    print(rate)


if __name__ == '__main__':
    # bot.run_bot()
    asyncio.run(get_weather())
    asyncio.run(get_volute())
