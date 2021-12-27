from db_handler import User, Word
from random import choice


def get_word_to_learn(chat_id):
    w = Word()
    user = User(user_id=chat_id)
    while True:
        w = w.get_random_word()
        if w.id not in user.learned:
            break
    return w


def get_word_to_repeat(chat_id):
    user = User(user_id=chat_id)
    if len(user.repeat):
        return Word(int(choice(user.repeat)))


def prepare_word_card(word, chat_id):
    user = User(user_id=chat_id)
    text = f"""
<i>Выучено: {len(user.learned)} из {500}</i>
<i>Для повторения: {len(user.repeat)}</i>
<i>({word.type} id: {word.id})</i>
--------------------------------------------
    
    <b>{str(word.eng).upper()}</b>

    <i>{word.transcript}</i>

    <b>{str(word.rus).upper()}</b>
    
    <b> </b>
    
    """

    return text


if __name__ == '__main__':
    w = get_word_to_repeat(105626824)
    print(prepare_word_card(w))
