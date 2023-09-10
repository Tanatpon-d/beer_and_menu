from pymongo import MongoClient
from datetime import datetime

class BeerLogger:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['beer_logs']
        self.collection = self.db['beer_logs']

    def log_action(self, action, beer_name):
        log_entry = {
            'timestamp': datetime.now(),
            'action': action,
            'beer_name': beer_name,
        }

        self.collection.insert_one(log_entry)

    def close(self):
        self.client.close()
