from fastapi import FastAPI
from typing import Union
import sqlite3
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str
    

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email : str

app = FastAPI()

@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "API REST"}

@app.get("/clientes/")
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response=cursor.fetchall()
        return response
        return {"message": "API REST"}