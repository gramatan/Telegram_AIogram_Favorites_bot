import asyncio
import logging
import asyncpg

from config import DB_CONNECTION, LDB_CONNECTION
from db import create_tables
from loader import bot, dp
import handlers.handlers

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    bot['db'] = await asyncpg.create_pool(dsn=DB_CONNECTION, min_size=3, max_size=5)

    await create_tables.run(bot['db'])
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await (await bot.get_session()).close()


if __name__ == '__main__':
    asyncio.run(main())
