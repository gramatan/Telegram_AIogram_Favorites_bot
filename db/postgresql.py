async def create_user(pool, user_id, user_first_name, username):
    sql = " INSERT INTO bot_users (id, first_name, username) VALUES ($1, $2, $3) ON CONFLICT DO NOTHING"
    await pool.execute(sql, user_id, user_first_name, username)


async def to_logs(pool):
    pass
