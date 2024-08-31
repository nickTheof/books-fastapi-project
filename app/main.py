from fastapi import FastAPI, HTTPException, status, Depends, Path
from contextlib import asynccontextmanager
from app.models import models
from app.database.database import Base, engine, get_db
from typing import Annotated
from sqlalchemy.orm import Session
from app.crud.crud import get_books, create_new_book, get_book_by_id, delete_book_by_id, update_book_by_id, get_books_by_rating
from app.schemas import schemas
from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/read-books", response_model=list[schemas.BookRead])
async def read_books(db: Annotated[Session, Depends(get_db)]):
    result = get_books(db=db)
    return result


@app.get("/read-books/{book_id}", response_model=schemas.BookRead)
async def read_book_by_id(book_id: int, db: Annotated[Session, Depends(get_db)]):
    db_book = get_book_by_id(db=db, id=book_id)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id: {book_id} is not found.')
    return db_book


@app.get('/read-books/rating/{rating}', response_model=list[schemas.BookRead])
async def read_books_by_rating(db: Annotated[Session, Depends(get_db)], rating: int = Path(ge=1, le=5)):
    db_books = get_books_by_rating(db=db, rating=rating)
    return db_books



@app.post("/create-book", response_model=schemas.BookRead)
async def create_book(db: Annotated[Session, Depends(get_db)], book: schemas.BookCreate):
    db_book = create_new_book(db=db, book=book)
    return db_book


@app.delete("/delete-book/{book_id}", response_class=JSONResponse)
async def delete_book(book_id: int, db: Annotated[Session, Depends(get_db)]):
    db_book = get_book_by_id(db=db, id=book_id)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id: {book_id} is not found.') 
    delete_book_by_id(db=db, id=id)
    return {'message': f'Book with id: {book_id} deleted successfully.'}



@app.put('/update-book/{book_id}', response_model=schemas.BookRead)
async def update_book(book_id: int, bookUpdate: schemas.BookUpdate, db: Annotated[Session, Depends(get_db)]):
    db_book = get_book_by_id(db=db, id=book_id)
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id: {book_id} is not found.') 
    new_db_book = update_book_by_id(db=db, id=book_id, updateBook=bookUpdate)
    return new_db_book


