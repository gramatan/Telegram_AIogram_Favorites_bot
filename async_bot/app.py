
import logging

from aiogram.types import ContentType
from aiogram.utils import executor

from config.config import LOCAL
from loader import dp
from handlers import handlers

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)


def register_handlers(dp):
    dp.register_message_handler(handlers.get_message_info, lambda message: message.text and 'getinfo' in message.text.lower() and message.from_user.id == LOCAL)
    dp.register_message_handler(handlers.saved_notes, lambda message: message.text and '#saved' in message.text.lower() and message.from_user.id == LOCAL)
    dp.register_message_handler(handlers.any_notes, lambda message: message.text and '#' in message.text.lower() and message.from_user.id == LOCAL)
    dp.register_message_handler(handlers.send_welcome, commands=['start', 'help'], user_id=LOCAL)
    dp.register_message_handler(handlers.send_dice, commands=['dice'])
    dp.register_message_handler(handlers.main_message_handler, content_types=ContentType.ANY, chat_id=LOCAL, user_id=LOCAL)

    dp.register_callback_query_handler(handlers.process_callback_notes, text='notes')
    dp.register_callback_query_handler(handlers.process_callback_saved2, text='saved2')
    dp.register_callback_query_handler(handlers.process_callback_learning, text='learning')
    dp.register_callback_query_handler(handlers.process_callback_lazada, text='lazada')
    dp.register_callback_query_handler(handlers.process_callback_family, text='family')
    dp.register_callback_query_handler(handlers.process_callback_saved3, text='saved3')
    dp.register_callback_query_handler(handlers.process_callback_cancel, text='cancel')



if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=False)
