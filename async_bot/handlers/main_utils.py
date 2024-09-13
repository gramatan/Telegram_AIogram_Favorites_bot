from aiogram import types


async def handle_sticker(message: types.Message):
    await message.answer(message.sticker.thumb.file_id)

async def handle_forwarded_message(message: types.Message):
    if not message.forward_date:
        return

    message_timestamp = message.forward_date.strftime('%Y-%m-%d %H:%M:%S')

    if message.forward_from_chat:
        message_link = f"https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}"
        message_data = f'<a href="{message_link}">{message.forward_from_chat.title}</a> at {message_timestamp}'
    elif message.forward_from:
        message_link = f"https://t.me/{message.forward_from.username}/{message.forward_from_message_id}"
        message_data = f'<a href="{message_link}">{message.forward_from.username}</a> at {message_timestamp}'
    else:
        message_data = f'{message.forward_sender_name} at {message_timestamp}'

    await message.answer(message_data, parse_mode='HTML')