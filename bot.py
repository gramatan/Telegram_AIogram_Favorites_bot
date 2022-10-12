import asyncio
import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.callback_data import CallbackData

from config import BOT_TOKEN

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
cb = CallbackData('keyboard', 'action')

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('button', callback_data='hello')]
])

keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('button', callback_data='hello'),
     InlineKeyboardButton('button2', callback_data='hello2')],
    [InlineKeyboardButton('button3', callback_data='hello'),
     InlineKeyboardButton('button4', callback_data='hello2')],
])


# handlers starts here
@dp.message_handler(lambda message: message.text and '#notes' in message.text.lower())
async def send_welcome(message: types.Message):
    await message.forward(chat_id=-886904261)


@dp.message_handler(lambda message: message.text and '#saved' in message.text.lower())
async def send_welcome(message: types.Message):
    await message.forward(chat_id=-708423371)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Just leave.', reply_markup=keyboard)


@dp.message_handler(commands='dice')
async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲')


@dp.callback_query_handler()
async def keyboard_callback_handler(callback: types.CallbackQuery):
    await callback.answer('something')


@dp.message_handler()
async def other(message: types.Message):
    if len(message.text.split(' ')) > 1:
        await message.reply(f'where to send your message({message.text.upper()})', reply_markup=keyboard2)
    else:
        await message.reply('message to short')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
