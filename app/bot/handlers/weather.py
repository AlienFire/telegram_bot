from aiogram import Dispatcher, types
from app.domane.service.weather import CityWeatherClient

async def get_weather(message: types.Message):
    """ Запрос погоды"""
    *_, city = message.text.split()

    weather_in_city = CityWeatherClient(city=city.title())
    await message.reply(await weather_in_city.city_weather())


def setup_handlers(dp: Dispatcher):
    """ функция для установки обработчиков"""
    dp.register_message_handler(get_weather, commands=['weather'])
