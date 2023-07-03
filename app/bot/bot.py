
import logging
from aiogram import Bot, Dispatcher, executor, types

from app.core.config import settings
from app.bot.handlers import init_handlers
# Configure logging
logging.basicConfig(level=logging.INFO)


def run_bot():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(bot)
    init_handlers(dp=dp)
    executor.start_polling(dp, skip_updates=True)
