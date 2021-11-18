import json


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
