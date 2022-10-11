import asyncio
import logging

from aiogram import Bot, Dispatcher, types, executor

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
bot = Bot(token='5777625302:AAE-3GYxBMzr6WkySFPOQQqqan4ZfBV1eSI')
dp = Dispatcher(bot)


@dp.message_handler(lambda message: message.text and '#notes' in message.text.lower())
async def send_welcome(message: types.Message):
    await message.forward(chat_id=-886904261)


@dp.message_handler(lambda message: message.text and '#saved' in message.text.lower())
async def send_welcome(message: types.Message):
    await message.forward(chat_id=-708423371)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Just leave.')


@dp.message_handler(commands='dice')
async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲')

@dp.message_handler(commands='list')
async def list_of_chats_with_user_and_bot:
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
