import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5777625302:AAE-3GYxBMzr6WkySFPOQQqqan4ZfBV1eSI')
dp = Dispatcher(bot)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message_handler(commands='start')
async def cmd_test1(message: types.message):
    await message.reply('start')


@dp.message_handler(commands='test1')
async def cmd_test1(message: types.message):
    await message.reply('test 1')


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
