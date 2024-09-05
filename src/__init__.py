from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    version=version,
    title="Book base",
    description="A simple book review service"
)

app.include_router(book_router, prefix=f'/api/{version}/books', tags="books")
