from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(published: bool,limit: int = 10, sort: Optional[str] = None) :
    if published:
        return {'data':f'{limit} published blogs'}
    else:
        return {'data':f'{limit} blogs'}

@app.get('/blog/unpublished')
def unpublished():
    return 'These are the list of unpublished blogs'

@app.get('/blog/{id}')
def about(id: int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {id:'This is the comment for this blog'}


class blog(BaseModel):
    title : str
    body : str
    published_date : Optional[bool]

@app.post('/predict')
def predict(request: blog):
    return request