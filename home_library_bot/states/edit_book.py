from aiogram.dispatcher.filters.state import StatesGroup, State

class NewBook(StatesGroup):
    Name = State()
    Author = State()
    Debtor = State()

class DeleteBook(StatesGroup):
    BookID = State()
    Confirm = State()