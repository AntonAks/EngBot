from aiogram import types
from loader import dp


# COMMON MESSAGE HANDLER
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"echo answer: {message['text']}")
