import json
import logging
import pytz
from bot import settings
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(settings.DB)


class Model(object):
    db = client.main_db

    def __init__(self, **kwargs):
        self.collection = kwargs['collection']

    def save(self):
        self.db[self.collection].insert_one({
            "item": self.item()
        })

    def __str__(self):
        return str(self.item())

    def item(self):
        return {i.replace(f"_{self.collection}__", ""): self.__dict__[i] for i in self.__dict__
                if i.startswith(f"_{self.collection}")}


class User(Model):

    def __init__(self):
        self.__id = None
        self.__timezone = str(pytz.timezone('Europe/Kiev'))
        super().__init__(collection=__class__.__name__)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def timezone(self):
        return self.__timezone

    @timezone.setter
    def timezone(self, value):
        self.__timezone = value

    def is_user_exist(self):
        check = Model.db[__class__.__name__].find_one({"item.id": self.__id})
        if check is None:
            return False
        return True

    def save(self):
        if self.is_user_exist():
            logging.warning(f"User is already exist")
        else:
            logging.warning(f"New user saved")
            super(User, self).save()

    @classmethod
    def get_all_users(cls):
        return list(cls.db[__class__.__name__].find())

    @classmethod
    def drop_collection(cls):
        cls.db[__class__.__name__].drop()


class Word(Model):
    pass


class Message(Model):
    def __init__(self):
        collection = __class__.__name__
        super().__init__(collection=collection)

