from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is running and is now live ....")
    await init_db()
    yield
    print(f"server has been stopped ....")

version = "v1"

app = FastAPI(
    version=version,
    title="Book base",
    description="A simple book review service",
    lifespan=life_span 
)

app.include_router(book_router, prefix=f'/api/{version}/books', tags="books")
