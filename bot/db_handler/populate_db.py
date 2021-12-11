from db_handler import Word
from tools import S3Helper

s3 = S3Helper()

if __name__ == '__main__':
    word_list = s3.get_words()

    w = Word()
    w.drop_all()
    for _w in word_list:
        word = Word()
        word.id = _w["id"]
        word.eng = _w["eng"]
        word.rus = _w["rus"]
        word.type = _w["type"]
        word.transcript = _w["transcript"]
        word.save()

    w = Word()
    print(w.get_all())
