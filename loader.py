from aiogram import Bot, Dispatcher
from aiogram.utils.callback_data import CallbackData

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
cb = CallbackData('keyboard', 'action')
dp = Dispatcher(bot)
