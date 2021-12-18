from aiogram import types


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    words_quiz_btn = types.InlineKeyboardButton(text="Learn Words", callback_data='learn_words')
    tense_tips_btn = types.InlineKeyboardButton(text="Tenses Tips", callback_data='tense_tips')
    other_grammar_tips_btn = types.InlineKeyboardButton(text="Other grammar tips", callback_data='other_grammar')

    keyboard.add(words_quiz_btn)
    keyboard.add(tense_tips_btn)
    keyboard.add(other_grammar_tips_btn)
    return keyboard
