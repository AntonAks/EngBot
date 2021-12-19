import re
from aiogram import types
from loader import dp
from db_handler import Message, User
from keyboards import main_keyboard
from loader import bot
from learn_engine import get_word_to_learn, get_word_to_repeat, prepare_word_card


# COMMAND HANDLERS
@dp.message_handler(commands=['start'])
async def _start_command(message: types.Message):
    user = User()
    user.id = message.from_user.id
    try:
        user.user_name = message.from_user.username
    except Exception:
        user.user_name = None
    user.save()
    await message.answer(f"Приветвствую! Сделайте ваш выбор.", reply_markup=main_keyboard())


@dp.message_handler(commands=['get_users'])
async def _get_users(message: types.Message):
    u = User()
    await message.answer(f"{u.get_all()}")


@dp.message_handler(commands=['del_users'])
async def _get_users(message: types.Message):
    u = User()
    u.drop_all()
    await message.answer(f"Пользователи удалены...")


# CALLBACK HANDLERS
@dp.callback_query_handler(lambda c: c.data in ['learn_words'])
async def learn_words(message: types.Message):
    chat_id = message["message"]["chat"]["id"]
    await bot.send_message(chat_id, "LEARN WORDS STARTED!!!")
    await get_learn_words(chat_id)


async def get_learn_words(chat_id):
    navigation_btns = types.InlineKeyboardMarkup()
    know = types.InlineKeyboardButton(text='✅ Знаю', callback_data='know')
    dontknow = types.InlineKeyboardButton(text='❌ Не знаю', callback_data='dontknow')
    navigation_btns.row(dontknow, know)
    word = get_word_to_learn(chat_id)
    word_card = prepare_word_card(word)

    await bot.send_message(chat_id,
                           word_card,
                           disable_notification=True,
                           parse_mode="html",
                           reply_markup=navigation_btns)


@dp.callback_query_handler(lambda c: c.data in ['dontknow', 'know'])
async def news_page_callback(call):
    chat_id = call.message.chat.id
    user = User(chat_id)
    print(user)
    print(user.item())
    text = call.message.text
    word_id = text[text.find('id: ') + len('id: '):text.rfind(')')]

    if call['data'] == "know":
        user.learned.append(word_id)
        user.update(chat_id)
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await get_learn_words(call["message"]["chat"]["id"])

    if call['data'] == "dontknow":
        user.repeat.append(word_id)
        user.update(chat_id)
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await get_learn_words(call["message"]["chat"]["id"])


@dp.callback_query_handler(lambda c: c.data in ['tenses_quiz'])
async def tenses_quiz(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "TENSES QUIZ STARTED!!!")


@dp.callback_query_handler(lambda c: c.data in ['tense_tips'])
async def tense_tips(message: types.Message):
    await bot.send_message(message["message"]["chat"]["id"], "TENSE TIPS !!!")


@dp.callback_query_handler(lambda c: c.data in ['other_grammar'])
async def other_grammar(message: types.Message):
    chat_id = message["message"]["chat"]["id"]
    await bot.send_message(chat_id, "OTHER GRAMMAR TIPS !!!")








# COMMON MESSAGE HANDLER
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     m = Message()
#     m.save()
#     await message.answer(f"echo answer: {message['text']}")



if __name__ == '__main__':
    print()
