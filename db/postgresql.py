from datetime import datetime

from aiogram import types


async def create_user(pool, message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    username = message.from_user.username
    sql = "INSERT INTO bot_users (id, first_name, username) VALUES ($1, $2, $3) ON CONFLICT DO NOTHING"
    await pool.execute(sql, user_id, user_first_name, username)


async def user_to_logs(pool, message: types.Message, **kwargs):
    sql = "INSERT INTO logs (datetime, user_id, type, action) VALUES ($1, $2, $3, $4)"

    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = message.from_user.id
    prefix = ''

    if kwargs:
        prefix = f'{kwargs}, '

    if message.forward_date:
        action_type = 3
        message_timestamp = message.forward_date.strftime('%Y-%m-%d %H:%M:%S')

        if message.forward_from_chat:
            message_data = f'{prefix}{message.forward_from_chat.title} at {message_timestamp}'
        else:
            message_data = f'{prefix}{message.forward_from.username} at {message_timestamp}'

    else:
        action_type = 1
        message_data = f'{prefix}{user} sent some message'

        await pool.execute(sql, date_time, user, action_type, message_data)
