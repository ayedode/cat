from fastapi import FastAPI, Request, HTTPException
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


def Titles():
    cursor.execute(
        "SELECT  id ,titles, url, author, category, date, imageurl, description FROM feed ORDER BY date DESC LIMIT 10;")   
    titles = cursor.fetchall()
    posts = []
    for title in titles:
        dict = {
            'id': title[0],
            'titles': title[1],
            'url': title[2],
            'author': title[3],
            'category': title[4],
            'date': title[5],
            'imageurl': title[6],
            'description': title[7]
        }
        posts.append(dict)
    return posts



def Tags():
    cursor.execute("SELECT tag,description FROM TAGS LIMIT 50;")
    all_tags = cursor.fetchall()
    tags  = []
    for title in all_tags:
        dict = {
            'tag': title[0],
            'description': title[1]
        }
        tags.append(dict)
    return tags


def CheckTagExsistence(tag):
    cursor.execute("SELECT tag FROM TAGS WHERE tag='{0}';".format(tag))
    tag = cursor.fetchall()
    if tag:
        return True
    else:
        return False


def TitlesTags(tag):
    logger.debug(tag + " Tag Requested")
    cursor.execute(
        "select feed.id,feed.titles, feed.url, feed.author, tags.tag, feed.date, feed.imageurl, feed.description from feed inner join connect on feed.id = connect.postid inner join tags on connect.tagsid = tags.id AND tags.tag='{0}';".format(tag))
    titles = cursor.fetchall()
    return titles


@app.get("/raw")
def root():
    cursor.execute("SELECT * FROM feed")
    records = cursor.fetchall()
    return{"POSTS": records}


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("item.html", {"request": request, "title": "All Post", "body_content": Titles()})


@app.get('/tags', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("tags.html", {"request": request, "title": "All Post", "body_content": Tags()})


@app.get("/tags/{tag_name}")
def get_tags_element(tag_name, request: Request):
    if CheckTagExsistence(tag_name):
        return templates.TemplateResponse("item.html", {"request": request, "title": "All Post", "body_content": TitlesTags(tag_name)})
    else:
        logger.debug(tag_name + " Tag Not Found")
        raise HTTPException(status_code=404, detail="%s Tag not Available" % tag_name,
                            headers={"X-Error": "Tag unavailable"},
                            )
