
from aiogram import Dispatcher
from .base import setup_handlers as setup_base_handlers
from .weather import setup_handlers as setup_weather_handlers
from .volute import setup_handlers as setup_volute_handlers

def init_handlers(dp:Dispatcher):
    setup_base_handlers(dp=dp)
    setup_weather_handlers(dp=dp)
    setup_volute_handlers(dp=dp)