from db_handler import Word
from random import shuffle, choice


class Quiz:
    questions_list = []

    def get_quiz_in_generator(self):
        return (q for q in self.questions_list)

    def get_quiz_in_list(self):
        return [q for q in self.questions_list]


class Question:
    text = None
    options = {}
    correct_answer = 0

    def __init__(self, text, options: list):
        self.text = text
        self.options = options

    def check_answer(self, value):
        if self.correct_answer == value:
            return True
        else:
            return False

    def __str__(self):
        return f"text: {self.text}, \n" \
               f"options: {self.options}, \n" \
               f"correct_answer {self.correct_answer}"


def get_options(word_id):

    w = Word()
    words_list = w.get_all()
    options = []
    options.append(word_id)
    while len(options) <= 4:
        option_word = choice(words_list)
        if word_id != option_word['id']:
            options.append(option_word['eng'])
    return options


def create_quiz():

    questions_list = []
    w = Word()
    words_list = w.get_all()
    shuffle(words_list)

    for word in words_list:
        options = get_options(word['id'])
        question = Question(text=word['rus'], options=options)
        questions_list.append(question)
    return questions_list


if __name__ == '__main__':
    q = create_quiz()

    for i in q:
        print(i)

