from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from decouple import config
import psycopg2
from loguru import logger


app = FastAPI()

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')


def connect():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
        logger.debug('Connected to Postgres')
        return conn
    except:
        logger.debug("Unable to connect to the database")


conn = connect()
cursor = conn.cursor()


class Post(BaseModel):
    ID: int
    titles: str
    URL: str
    Author: str
    category: Optional[str] 
    date: Optional[str]

@app.get("/all")
def root():
   cursor.execute("SELECT * FROM feed")
   records = cursor.fetchall()  
   return{"POSTS": records}


# @app.post("/itemgs")
# def create(payLoad: Post):
#     print(payLoad.title)
#     print(payLoad.dict())
#     return {"data": payLoad}



# @app.get("/items/{item_id}")
# def read_item(item_id: int,):
#     return {"item_id": item_id}


# conn.commit()
# conn.close()
