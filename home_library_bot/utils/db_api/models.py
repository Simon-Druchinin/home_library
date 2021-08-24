from sqlalchemy import (Column, Integer, String, Sequence)
from sqlalchemy import sql
from utils.db_api.database import db

#make a book table class
class Book(db.Model):
    __tablename__ = 'books'
    query: sql.Select

    #book id
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    #name, author, photo and debtor
    name = Column(String(50))
    author = Column(String(50))
    photo = Column(String(250))
    debtor = Column(String(50))

    def __repr__(self):
        return f"""
Книга № {self.id} - "{self.name}"
Должник: {self.debtor}"""