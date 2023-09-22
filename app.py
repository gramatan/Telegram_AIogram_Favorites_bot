import asyncio
import logging

from loader import bot, dp
import handlers.handlers

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await (await bot.get_session()).close()


if __name__ == '__main__':
    asyncio.run(main())
