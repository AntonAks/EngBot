import json
import logging
import pytz
import settings
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(settings.DB)
db = client.main_db


class Model(object):
    def __init__(self, **kwargs):
        print(">>>", kwargs['collection'], kwargs['db'])
        self.db = kwargs['db']
        self.collection = kwargs['collection']

    def save(self, value):
        message_dict = json.loads(str(value))
        self.db[self.collection].insert_one({
            "message": message_dict
        })


class User(Model):

    def __init__(self, **kwargs):
        self._name = None
        self._timezone =
        super().__init__(collection=__class__.__name__, db=db)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        self._timezone = value


class Word(Model):
    pass


class Message(Model):
    def __init__(self, **kwargs):
        # collection = db[__class__.__name__]
        collection = __class__.__name__
        super().__init__(collection=collection, db=db)

