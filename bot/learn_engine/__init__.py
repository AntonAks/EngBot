from db_handler import User, Word


def get_word_to_learn(chat_id):
    w = Word()
    user = User(user_id=chat_id)
    while True:
        w = w.get_random_word()
        if w.id not in user.learned:
            break
    return w


def get_word_to_repeat(chat_id):
    w = Word()
    user = User(user_id=chat_id)
    while True:
        w = w.get_random_word()
        if w.id not in user.repeat:
            break
    return w


def prepare_word_card(word):
    text = f"""
    <b>{str(word.eng).upper()}  -  {word.transcript}</b>

<b>{word.rus}</b>

<i>({word.type} id: {word.id})</i>
    """

    return text


if __name__ == '__main__':
    w = get_word_to_learn(105626824)
    print(prepare_word_card(w))
