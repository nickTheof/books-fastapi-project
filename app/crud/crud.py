from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_books(db: Session) -> models.Books | None:
    books = db.query(models.Books)
    return books


def create_new_book(db: Session, book: schemas.BookCreate) -> models.Books | None:
    db_book = models.Books(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book_by_id(db: Session, id: int) -> models.Books | None:
    db_book = db.query(models.Books).filter_by(id=id).first()
    return db_book


def get_books_by_rating(db: Session, rating: int) -> models.Books | None:
    db_book = db.query(models.Books).filter_by(rating=rating).all()
    return db_book

def delete_book_by_id(db: Session, id: int) -> None:
    db_book = db.query(models.Books).filter_by(id=id).first()
    db.delete(db_book)
    db.commit()


def update_book_by_id(db: Session, id: int, updateBook: schemas.BookUpdate) -> models.Books | None:
    db_book = db.query(models.Books).filter_by(id=id).first()
    db_book.description = updateBook.description
    db_book.rating = updateBook.rating
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book