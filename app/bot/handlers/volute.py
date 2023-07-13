from aiogram import Dispatcher, types
from app.domane.service.volute import VoluteClient

async def get_volute(message: types.Message):
    """ Запрос курса валюты"""
    *_, volute_data = message.text.split()

    exchange_rate = VoluteClient(volute_data=volute_data.upper())
    await message.reply(await exchange_rate.get_value())


def setup_handlers(dp: Dispatcher):
    """ функция для установки обработчиков"""
    dp.register_message_handler(get_volute, commands=['rate'])