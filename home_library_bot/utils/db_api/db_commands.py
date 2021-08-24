from typing import List

from utils.db_api import Book
from utils.db_api.database import db


# Creating a new Book instance function. Takes all arguments from Book
async def add_book(**kwargs):
    new_book = await Book(**kwargs).create()
    return new_book

#get all books
async def get_all_books() -> List[Book]:
    book = await Book.gino.all()
    return book

#get borrowed books
async def get_borrowed_books() -> List[Book]:
    book = await Book.query.where(
        (Book.debtor != None)
    ).gino.all()
    return book

#get book by id function
async def get_book(book_id) -> Book:
    book = await Book.query.where(Book.id == book_id).gino.first()
    return book
