from fastapi import FastAPI,Query
from DAL import DataLoader
from solider import Solider

app = FastAPI()


uri = "mongodb://mongodb:27017"
loader=DataLoader(uri)


@app.get("/")
def home():
    return {"message": "hello"}

@app.get("/data")
def get_data():
    return loader.get_all()


@app.get("/insert/")
def add_soldier(
    id = Query(...),
    first_name = Query(...),
    last_name = Query(...),
    phone_number = Query(...),
    rank = Query(...)
):
    soldier = Solider(id, first_name, last_name, phone_number, rank)
    loader.insert(soldier)
    return {"message": "yyyyy"}

@app.get("/delete/")
def delete_data(
    id = Query(...)
    ):
    
    return loader.delete(id)



@app.get("/update/")
def update_data(
    id = Query(...),
    field=Query(...),
    value=Query(...)
    ):
    return loader.update(id,field,value)


