from datetime import datetime
from zoneinfo import ZoneInfo

async def create_user(pool, message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    username = message.from_user.username
    sql = "INSERT INTO bot_users (id, first_name, username) VALUES ($1, $2, $3) ON CONFLICT DO NOTHING"
    await pool.execute(sql, user_id, user_first_name, username)


async def user_to_logs(pool, message, prefix=None):
    if prefix:
        prefix = f'{prefix},'
    sql = "INSERT INTO logs (datetime, user, type, action) VALUES ($1, $2, $3, $4)"
    date_time = datetime.now(tz=ZoneInfo('UTC'))
    user = message.from_user.id

    if message.chat.id < 0:
        action_type = 2
    elif message.forward_from:
        action_type = 3
    else:
        action_type = 2

    action = f'{prefix}'


