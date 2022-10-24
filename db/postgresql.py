import asyncio
import asyncpg
import asyncpgsa


async def create_user(pool, user_id, user_first_name, username):
    sql = " INSERT INTO bot_users (id, first_name, username) VALUES ($1, $2, $3) ON CONFLICT DO NOTHING"
    await pool.execute(sql, user_id, user_first_name, username)


# async def create_pool_on_startup(pool):
#     pool = asyncpg.create_pool(
#         user=DB_USER,
#         password=DB_PASS,
#         host=DB_HOST,
#         port=DB_PORT
#     )
#     await pool
#
#
#     await pool.close()
