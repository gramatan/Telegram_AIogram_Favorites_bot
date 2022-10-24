from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(inline_keyboard=[])

keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('notes', callback_data='notes'),
     InlineKeyboardButton('saved2', callback_data='saved2'),
     InlineKeyboardButton('learning', callback_data='learning')],
    [InlineKeyboardButton('saved3', callback_data='saved3'),
     InlineKeyboardButton('lazada', callback_data='lazada'),
     InlineKeyboardButton('family', callback_data='family')],
    [InlineKeyboardButton('Done', callback_data='cancel')],
])