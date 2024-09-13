from aiogram import types

from config.config import ADMIN, NOTES, SAVED2, LEARNING, SAVED3, LAZADA, FAMILY1, HELP
from handlers.main_utils import handle_sticker, handle_forwarded_message
from keyboards.keyboards import main_keyboard, blank_keyboard
from loader import bot


# one handler for debug them all. plus test add user
async def get_message_info(message: types.Message):
    await bot.send_message(chat_id=ADMIN, text=message)


# message handlers starts here
async def saved_notes(message: types.Message):
    await message.send_copy(chat_id=SAVED2, disable_notification=True)
    await message.delete()


async def any_notes(message: types.Message):
    await message.send_copy(chat_id=NOTES, disable_notification=True)

async def send_welcome(message: types.Message):
    await message.answer(text=HELP)


async def send_dice(message: types.Message):
    await message.answer_dice(emoji='🎲', disable_notification=True)
    await message.delete()

# main handler
async def main_message_handler(message: types.Message):
    if message.chat.id > 0:
        if message.sticker:
            await handle_sticker(message)

        await handle_forwarded_message(message)

        await message.send_copy(chat_id=message.chat.id, reply_markup=main_keyboard, disable_notification=True)
        await message.delete()


# Query handlers
async def process_callback_notes(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=NOTES, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to notes')


async def process_callback_saved2(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED2, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to saved2')


async def process_callback_learning(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LEARNING, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to learning', disable_notification=True)


async def process_callback_lazada(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=LAZADA, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to lazada', disable_notification=True)


async def process_callback_family(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=FAMILY1, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()
    await callback_query.message.answer('sent to family', disable_notification=True)


async def process_callback_saved3(callback_query: types.CallbackQuery):
    await callback_query.message.send_copy(chat_id=SAVED3, reply_markup=blank_keyboard, disable_notification=True)
    await callback_query.message.delete()


async def process_callback_cancel(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Галя, у нас отмена!')
    await callback_query.message.delete()
