from pymongo import MongoClient

class DataLoader:
    def __init__(self, uri: str, db_name: str = "mydb"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["data"]

    def init_data(self):
        if self.collection.count_documents({}) == 0:
            docs = [
                {"ID": 1, "first_name": "Itamar", "last_name": "Levi"},
                {"ID": 2, "first_name": "Noa", "last_name": "Cohen"},
                {"ID": 3, "first_name": "Avi", "last_name": "Bar"},
                {"ID": 4, "first_name": "Dana", "last_name": "Shalev"},
                {"ID": 5, "first_name": "Ron", "last_name": "Shamir"},
            ]
            self.collection.insert_many(docs)

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))