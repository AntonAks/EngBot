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
