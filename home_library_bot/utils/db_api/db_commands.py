from typing import List

from utils.db_api.models import Book
from sqlalchemy.sql.expression import Delete

# Creating a new Book instance function. Takes all arguments from Book
async def add_book(**kwargs):
    new_book = await Book(**kwargs).create()
    return new_book

#get all books
async def get_all_books() -> List[Book]:
    book = await Book.query.gino.all()
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

#delete book
async def delete_book(book_id):
    await Book.delete.where(Book.id == book_id).gino.status()