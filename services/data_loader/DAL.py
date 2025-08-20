from pymongo import MongoClient ,errors
from solider import Solider

class DataLoader:
    def __init__(self, uri: str, db_name: str = "mydb"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["data"]

    def insert(self,solider:Solider):
        try:
            self.collection.insert_one(solider.__dict__)
            return True
        except errors.DuplicateKeyError:
            print("id is exist")
        except Exception as e:
            print(f"error: {e}")

    def get_all(self):
        try:
            res= list(self.collection.find({}, {"_id": 0}))
            print(res)
            return res
        except Exception as e:
            print(f"error: {e}")
    
    
    def update(self,id,field,value):
        try:
            res=self.collection.update_one({"id":id},{"$set":{field:value}})
            return res.modified_count
        except Exception as e:
            print(f"error: {e}")
        
    def delete(self,id):
        try:
            res=self.collection.delete_one({"id":id})
            return res.deleted_count
        except Exception as e:
            print(f"error: {e}")
        