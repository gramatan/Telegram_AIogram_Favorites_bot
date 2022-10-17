import asyncio
import logging

from datetime import datetime

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.callback_data import CallbackData

from config import BOT_TOKEN, LOCAL, NOTES, SAVED2, LEARNING, SAVED3, LAZADA, FAMILY1, HELP

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
cb = CallbackData('keyboard', 'action')

keyboard = InlineKeyboardMarkup(inline_keyboard=[])

keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('notes', callback_data='notes'),
     InlineKeyboardButton('saved2', callback_data='saved2'),
     InlineKeyboardButton('learning', callback_data='learning')],
    [InlineKeyboardButton('saved3', callback_data='saved3'),
     InlineKeyboardButton('lazada', callback_data='lazada'),
     InlineKeyboardButton('family', callback_data='family')],
])


# one handler for debug them all
@dp.message_handler(lambda message: message.text and 'getinfo' in message.text.lower())
async def start_process(message: types.Message):
    await message.reply(message)


# message handlers starts here
@dp.message_handler(lambda message: message.text and '#notes' in message.text.lower())
async def start_process(message: types.Message):
    await message.send_copy(chat_id=NOTES, disable_notification=True)
    await message.delete()


@dp.message_handler(lambda message: message.text and '#saved' in message.text.lower())
async def send_welcome(message: types.Message):
    await message.send_copy(chat_id=SAVED2, disable_notification=True)
    await message.delete()


@dp.message_handler(commands=['start', 'help'], chat_id=LOCAL)
async def send_welcome(message: types.Message):
    await message.answer(text=HELP)


@dp.message_handler(lambda message: message.text and 'dice' in message.text.lower())
async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲', disable_notification=True)


# main handler
@dp.message_handler(content_types=ContentType.ANY, chat_id=LOCAL)
async def other(message: types.Message):
    if message.forward_date:
        message_timestamp = message.forward_date.strftime('%Y-%m-%d %H:%M:%S')
        message_data = f'{message.forward_from_chat.title} at {message_timestamp}'
        await message.answer(message_data)
    await message.send_copy(chat_id=LOCAL, reply_markup=keyboard2, disable_notification=True)
    await message.delete()


# Query handlers
@dp.callback_query_handler(text='notes')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=NOTES, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to notes')


@dp.callback_query_handler(text='saved2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED2, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to saved2')


@dp.callback_query_handler(text='learning')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LEARNING, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to learning', disable_notification=True)


@dp.callback_query_handler(text='lazada')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LAZADA, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to lazada', disable_notification=True)


@dp.callback_query_handler(text='family')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=FAMILY1, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to family', disable_notification=True)


@dp.callback_query_handler(text='saved3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED3, reply_markup=keyboard, disable_notification=True)
    await callback_query.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
