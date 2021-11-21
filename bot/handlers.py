from aiogram import types
from loader import dp
import keyboards as kb
from tzwhere import tzwhere

@dp.message_handler(content_types=['text'])
async def request_location(message: types.Message):
    await message.answer('Для направления уведомлений нам нужно знать Ваш часовой пояс. \n'
                         'Пожалуйста укажите свою геолокацию.', reply_markup=kb.markup_request_location)

@dp.message_handler(content_types=['location'])
async def handle_loc(message):
    tz = tzwhere.tzwhere()
    timezone = tz.tzNameAt(message.location['latitude'], message.location['longitude'])
    print(timezone)


# COMMON MESSAGE HANDLER
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(f"echo answer: {message['text']}")
