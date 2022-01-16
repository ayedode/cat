Create App:
```
app = FastAPI()
```

Create Pydantic Model to Verify POST Request
```
class Post(BaseModel):
    title: str
    content: str
    Published: bool = True
    rating: Optional[int] = None
```

Get Request on `/` endpoint: 
```
@app.get("/")
async def root():
    return {"message":"Hello World!!!"}
```

Post Request 
```
@app.post("/items")
def create(payLoad: Post):
    print(payLoad.title)
    print(payLoad.dict()) # Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
    return {"data": payLoad}
```    