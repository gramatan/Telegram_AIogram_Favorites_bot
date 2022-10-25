import asyncio
import logging
import asyncpg

from config import DB_NAME, DB_HOST, DB_PASS, DB_PORT, DB_USER
from db import create_tables
from loader import bot, dp
import handlers.handlers    # important shit. do not del

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    bot['db'] = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        min_size=3,
        max_size=5
    )
    await create_tables.run(bot['db'])
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await (await bot.get_session()).close()


if __name__ == '__main__':
    asyncio.run(main())
