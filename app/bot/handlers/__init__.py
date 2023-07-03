
from aiogram import Dispatcher
from .base import setup_handlers


def init_handlers(dp:Dispatcher):
    setup_handlers(dp=dp)