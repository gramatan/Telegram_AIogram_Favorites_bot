import asyncio
import asyncpg

from config import DB_CONNECTION


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(DB_CONNECTION)
        )

    async def crete_user(self, user_id, user_first_name, username):
        sql = " INSERT INTO users (id, first_name, username) VALUES ($1, $2, $3)"
        await self.pool.execute(sql, user_id, user_first_name, username)
