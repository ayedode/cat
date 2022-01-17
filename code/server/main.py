from typing import Optional
from fastapi import FastAPI, Request
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from decouple import config
import psycopg2
from loguru import logger
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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


def Titles():
    cursor.execute("SELECT titles FROM feed")
    titles = cursor.fetchall()
    all=[]
    for list in titles:
        for sublist in list:
            all.append(sublist)
    return all

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("item.html", {"request": request, "title": "All Post", "body_content": Titles()})


@app.get("/raw")
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
