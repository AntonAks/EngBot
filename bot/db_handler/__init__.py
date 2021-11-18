import json
import logging
import pytz
import settings
from datetime import datetime
from pymongo import MongoClient
from . mongo_model import Model


default_tz = str(pytz.timezone('Europe/Kiev'))

client = MongoClient(settings.DB)
db = client.main_db


class User:
    pass


class Word:
    pass


class Message(Model):
    def __init__(self, **kwargs):
        # collection = db[__class__.__name__]
        collection = __class__.__name__
        super().__init__(collection=collection, db=db)


if __name__ == '__main__':
    m = Message()
