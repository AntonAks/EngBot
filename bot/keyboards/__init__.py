from aiogram import types


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    words_quiz_btn = types.InlineKeyboardButton(text="Words Quiz", callback_data='words_quiz')
    tense_quiz_btn = types.InlineKeyboardButton(text="Tenses Test", callback_data='tenses_quiz')
    tense_tips_btn = types.InlineKeyboardButton(text="Tenses Tips", callback_data='tense_tips')
    other_grammar_tips_btn = types.InlineKeyboardButton(text="Other grammar tips", callback_data='other_grammar')

    keyboard.add(words_quiz_btn)
    keyboard.add(tense_quiz_btn)
    keyboard.add(tense_tips_btn)
    keyboard.add(other_grammar_tips_btn)
    return keyboard
