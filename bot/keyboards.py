from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_request_location = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Передать геолокацию', request_location=True))

