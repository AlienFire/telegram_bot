from aiogram import Dispatcher, types

async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def echo(message: types.Message):
    '''Just echo'''
    await message.answer(message.text)


async def greating(message: types.Message):
    await message.reply('Hello!')

def setup_handlers(dp:Dispatcher):
    """ функция для установки обработчиков"""
    dp.register_message_handler(send_welcome,commands=['start', 'help'])
    dp.register_message_handler(greating, lambda msg: 'hello' in msg.text.lower())
    dp.register_message_handler(echo)
