import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5777625302:AAE-3GYxBMzr6WkySFPOQQqqan4ZfBV1eSI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Hello World')


@dp.message_handler(commands='test1')
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message_handler(commands='dice')
async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲')

if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)