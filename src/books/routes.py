from fastapi import status, APIRouter
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import Book, BookUpateModel
from typing import List


book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_all_books():
    return books

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}', status_code=status.HTTP_200_OK)
async def get_all_books(book_id:int) -> dict:
    for book in books: 
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with the id of {book_id}")

@book_router.patch('/{book_id}', status_code=status.HTTP_200_OK)
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

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int): 
    for book in books: 
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book with the id of {book_id}")