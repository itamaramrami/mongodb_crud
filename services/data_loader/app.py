from fastapi import FastAPI
from DAL import DataLoader
from solider import Solider
import os

app = FastAPI()


uri = "mongodb://localhost:27017"

# loader = DataLoader(uri)
# solid=Solider(2,"it","kk",12,"ll")
# loader.insert(solid)
# loader.delete(1)
# loader.get_all()
# loader.update(1,"rank","ooo")

@app.get("/data")
def get_data():
    return loader.get_all()
