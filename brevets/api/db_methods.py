"""
Various methods for MongoDB
"""
import os
from pymongo import MongoClient
import config


class Db:

    def __init__(self):
        self.client = MongoClient(
            'mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
        self.db = self.client.brevetdb  # name of the database we're using

    def find_content(self, *args, **kwargs):
        return self.db.brevetcoll.find(*args, **kwargs)
