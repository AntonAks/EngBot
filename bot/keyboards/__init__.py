from aiogram import types


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    words_learn_btn = types.InlineKeyboardButton(text="Проверить слова", callback_data='check_words')
    words_repeat_btn = types.InlineKeyboardButton(text="Повторитьы слова", callback_data='repeat_words')
    tense_tips_btn = types.InlineKeyboardButton(text="Учить времена", callback_data='tense_tips')
    other_grammar_tips_btn = types.InlineKeyboardButton(text="Друшая грамматика", callback_data='other_grammar')

    keyboard.add(words_learn_btn)
    keyboard.add(words_repeat_btn)
    # keyboard.add(tense_tips_btn)
    # keyboard.add(other_grammar_tips_btn)
    return keyboard
