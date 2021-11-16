from aiogram import types
from loader import dp
import keyboards as kb


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer('Подскажите Вашу геолокацию', reply_markup=kb.markup_request)


# COMMON MESSAGE HANDLER
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(f"echo answer: {message['text']}")
