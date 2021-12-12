import json
import logging
import pytz
import settings
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(settings.DB)


class Model(object):
    db = client.engbot_db

    def __init__(self):
        self.collection = self.__name__

    def __str__(self):
        return str(f"{type(self)}, {self.item()}")

    def save(self):
        self.db[self.collection].insert_one({
            "item": self.item()
        })

    def item(self) -> dict:
        return {i: self.__dict__[i] for i in self.__dict__ if i != 'collection'}

    def get_all(self) -> list:
        items = [i['item'] for i in list(self.db[self.__name__].find())]
        return items

    def drop_all(self):
        self.db[self.__name__].drop()


class User(Model):
    __name__ = 'users'

    def __init__(self, user_id=None):
        if user_id is None:
            self.id = None
            self.timezone = str(pytz.timezone('Europe/Kiev'))
        else:
            self._get_user_from_db(user_id)
        super().__init__()

    def is_user_exist(self):
        check = Model.db[__class__.__name__].find_one({"item.id": self.id})
        if check is None:
            return False
        return True

    def save(self):
        if self.is_user_exist():
            logging.warning(f"User is already exist")
        else:
            logging.warning(f"New user saved")
            super(User, self).save()

    def _get_user_from_db(self, user_id):
        user = Model.db[__class__.__name__].find_one({"item.id": user_id})
        self.id = user['item']['id']
        self.timezone = user['item']['timezone']


class Word(Model):
    __name__ = 'users'

    def __init__(self, word_id=None):

        if word_id is None:
            self.id = None
            self.type = None
            self.rus = None
            self.eng = None
            self.transcript = None
        else:
            self._get_word_from_db(word_id)
        super().__init__()

    def _get_word_from_db(self, word_id):
        word = Model.db[__class__.__name__].find_one({"item.id": word_id})
        self.id = word['item']['id']
        self.type = word['item']['type']
        self.rus = word['item']['rus']
        self.eng = word['item']['eng']
        self.transcript = word['item']['transcript']


class Message(Model):
    __name__ = "messages"

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    w = Word()

    for i in w.get_all():
         w = Word(i['id'])
         print(w)