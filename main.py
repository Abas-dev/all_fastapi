from fastapi import FastAPI
from typing import Optional

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
async def greet_name_02(name:Optional[str]='User', age:int=0) -> dict:
    return {'message':f'hello {name}, you are {age} years old'}