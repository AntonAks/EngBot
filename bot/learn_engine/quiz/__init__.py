from db_handler import Word
from random import shuffle, choice


class Question:
    word = None
    options = []

    def __init__(self, text, options: list):
        self.text = text
        self.options = options

    def check_answer(self, value):
        if self.word == value:
            return True
        else:
            return False

    def __str__(self):
        return f"word: {self.text} options: {self.options}"


def get_options(word_id):

    w = Word()
    words_list = w.get_all()
    options = []
    options.append(Word(word_id))
    while len(options) < 4:
        option_word = choice(words_list)
        if option_word['id'] not in [w.id for w in options] and option_word['type'] in [w.type for w in options]:
            options.append(Word(option_word['id']))
    return options


def create_quiz():

    questions_list = []
    w = Word()
    words_list = w.get_all()
    shuffle(words_list)

    for word in words_list:
        options = get_options(word['id'])
        question = Question(text=Word(word['id']), options=options)
        questions_list.append(question)
    return questions_list


if __name__ == '__main__':
    q = create_quiz()


