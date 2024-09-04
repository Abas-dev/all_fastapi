from fastapi import FastAPI, Header
from typing import Optional

from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {'message':'hello world'}

@app.get('/path_greet/{name}')
async def greet_name(name:str) -> dict:
    return {'message':f'hello {name}'}

@app.get('/query_greet')
async def greet_name_01(name:str) -> dict:
    return {'message':f'hello {name}'}

@app.get('/greet/{name}')
async def greet_name_02(name:str, age:int) -> dict:
    return {'message':f'hello {name}, you are {age} years old'}

'''  this is to make the path parameter optional using python Optional class from typing '''
@app.get('/optional_greet')
async def greet_name_03(name:Optional[str]='User', age:int=0) -> dict:
    return {'message':f'hello {name}, you are {age} years old'}


'''i am starting to use post request from here to be sendig data from the request body'''

class BookCreateModel(BaseModel):
    title : str 
    author : str

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        'title': book_data.title,
        'author': book_data.author
    }

@app.get('/get_headers', status_code=200)
async def get_headers(accept:str = Header(None), 
                      content_type:str = Header(None), 
                      user_agent:str = Header(None),
                      host:str = Header(None),
):
    request_headers = {}

    request_headers['Accept'] = accept
    request_headers['Content_Type'] = content_type
    request_headers['User-Agent'] = user_agent
    request_headers['Host'] = host

    return request_headers 