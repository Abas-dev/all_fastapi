from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


books = [
    {   
        "id":1,
        "title":"Thank Your Lucky Stars",
        "author":"Maurits Bartlam",
        "publisher":"Winnie Earengey",
        "published_date":"8/7/2024",
        "page_count":'8543',
        "language":"Gujarati"
    },
    {   
        "id":2,
        "title":"Moscow Does Not Believe in Tears (Moskva slezam ne verit)",
        "author":"Eben Romaines",
        "publisher":"Rooney Pecht",
        "published_date":"6/15/2024",
        "page_count":'34733',
        "language":"Papiamento"
    },
    {   
        "id":3,
        "title":"Make Mine Music",
        "author":"Dorothee Meeks",
        "publisher":"Sutton Vanyashin",
        "published_date":"5/15/2024",
        "page_count":'5676',
        "language":"Montenegrin"
    },
    {   
        "id":4,
        "title":"Pudana Last of the Line (Sukunsa viimeinen)",
        "author":"Arni Runham",
        "publisher":"Marinna Trawin",
        "published_date":"6/7/2024",
        "page_count":'6533',
        "language":"Polish"
    },
    {   
        "id":5,
        "title":"Girls in Prison",
        "author":"Billie Hale",
        "publisher":"Abbot Pevreal",
        "published_date":"7/24/2024",
        "page_count":'2353',
        "language":"Hebrew"
    },
]

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date: str
    page_count:int
    language:str

class BookUpateModel(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:int
    language:str

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def get_all_books(book_id:int) -> dict:
    for book in books: 
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with the id of {book_id}")

@app.patch('/books/{book_id}', status_code=status.HTTP_200_OK)
async def update_a_book(book_id:int, bookUpdateData:BookUpateModel) -> dict:
    for book in books: 
        if book['id'] == book_id:
            book['title'] = bookUpdateData.title
            book['author'] = bookUpdateData.author
            book['publisher'] = bookUpdateData.publisher
            book['page_count'] = bookUpdateData.page_count
            book['language'] = bookUpdateData.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No book with the id of {book_id}')    

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int): 
    for book in books: 
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with the id of {book_id}")