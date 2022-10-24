from aiogram import Dispatcher, types
from aiogram.types import ContentType

from config import LOCAL, NOTES, SAVED2, LEARNING, SAVED3, LAZADA, FAMILY1, HELP
from keyboards.keyboards import blank_keyboard, main_keyboard
from loader import dp, bot
from db import postgresql


# one handler for debug them all. plus test add user
@dp.message_handler(lambda message: message.text and 'getinfo' in message.text.lower())
async def get_message_info(message: types.Message):
    # await message.reply(message)

    await bot.send_message(chat_id=LOCAL, text=message)


@dp.message_handler(commands='add_user', chat_id=LOCAL)
async def create_new_user(message: types.Message):
    await postgresql.create_user(bot['db'], message)
    await message.answer('user created')


# message handlers starts here
@dp.message_handler(lambda message: message.text and '#saved' in message.text.lower())
async def saved_notes(message: types.Message):
    await message.send_copy(chat_id=SAVED2, disable_notification=True)
    await postgresql.user_to_logs(bot['db'], message, prefix='#saved')
    await message.delete()


@dp.message_handler(lambda message: message.text and '#' in message.text.lower())
async def any_notes(message: types.Message):
    await message.send_copy(chat_id=NOTES, disable_notification=True)
    await postgresql.user_to_logs(bot['db'], message, prefix='#notes')


@dp.message_handler(commands=['start', 'help'], chat_id=LOCAL)
async def send_welcome(message: types.Message):
    await message.answer(text=HELP)


@dp.message_handler(lambda message: message.text and 'dice' in message.text.lower())
async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲', disable_notification=True)


# main handler
# @dp.message_handler(content_types=ContentType.ANY, chat_id=LOCAL, user_id=LOCAL)
@dp.message_handler(content_types=ContentType.ANY)
async def main_message_handler(message: types.Message):
    if message.chat.id > 0:
        chat_id = message.chat.id
        if message.sticker:
            await message.answer(message.sticker.thumb.file_id)
        if message.forward_date:
            message_timestamp = message.forward_date.strftime('%Y-%m-%d %H:%M:%S')
            if message.forward_from_chat:
                message_data = f'{message.forward_from_chat.title} at {message_timestamp}'
            else:
                message_data = f'{message.forward_from.username} at {message_timestamp}'
            await message.answer(message_data)
        await message.send_copy(chat_id=chat_id, reply_markup=main_keyboard, disable_notification=True)
        await postgresql.user_to_logs(bot['db'], message)
        await message.delete()


# Query handlers
@dp.callback_query_handler(text='notes')
async def process_callback_notes(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=NOTES, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to notes')


@dp.callback_query_handler(text='saved2')
async def process_callback_saved2(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED2, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to saved2')


@dp.callback_query_handler(text='learning')
async def process_callback_learning(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LEARNING, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to learning', disable_notification=True)


@dp.callback_query_handler(text='lazada')
async def process_callback_lazada(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LAZADA, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to lazada', disable_notification=True)


@dp.callback_query_handler(text='family')
async def process_callback_family(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=FAMILY1, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to family', disable_notification=True)


@dp.callback_query_handler(text='saved3')
async def process_callback_saved3(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED3, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()


@dp.callback_query_handler(text='cancel')
async def process_callback_cancel(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Галя, у нас отмена!')
    await callback_query.message.delete()