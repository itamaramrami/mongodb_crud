from fastapi import FastAPI
from .DAL import *
import os

app = FastAPI()

MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASS = os.getenv("MONGO_PASS", "root123")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo-service")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"

loader = DataLoader(uri)
loader.init_data()

@app.get("/data")
def get_data():
    return loader.get_all()
