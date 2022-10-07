import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5777625302:AAE-3GYxBMzr6WkySFPOQQqqan4ZfBV1eSI')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handlers(commands='test1')
async def cmd_test1(message: types.message):
    await message.reply('test 1')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
