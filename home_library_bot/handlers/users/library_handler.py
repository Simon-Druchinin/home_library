from typing import Union
from utils.db_api.models import Book

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from states.edit_book import NewBook, DeleteBook
from loader import dp

from utils.db_api.db_commands import delete_book, get_borrowed_books
from keyboards.inline.book_keyborads import delete_debtor_keyboard, cancel_keyboard, confirm_keyboard, show_debtors_keyboard

async def call_main_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    markup = await show_debtors_keyboard()
    await call.message.answer_photo(photo=open('files/images/books.jpg', 'rb'), reply_markup=markup)

async def message_main_menu(message: Message):
    markup = await show_debtors_keyboard()
    await message.answer_photo(photo=open('files/images/books.jpg', 'rb'), reply_markup=markup)

@dp.callback_query_handler(text_contains='cancel', state='*')
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Вы отменили создание книги')
    await call_main_menu(call)
    await state.reset_state()

@dp.callback_query_handler(text_contains='show_debtors')
async def show_items(call: CallbackQuery):
    await call.message.edit_reply_markup()
    markup = await delete_debtor_keyboard()
    books = await get_borrowed_books()
    text=''
    for num, book in enumerate(books):
        text += f'{book}\n\n'
    if text == '':
        markup = await show_debtors_keyboard()
        await call.message.answer('У вас нет должников.', reply_markup=markup)
    else:
        await call.message.answer(text, reply_markup=markup)

@dp.callback_query_handler(text_contains='add_debtors')
async def add_book(call: CallbackQuery):
    await call.message.edit_reply_markup()
    markup = await cancel_keyboard()
    await call.message.answer('Введите название книги', reply_markup=markup)
    await NewBook.Name.set()

@dp.message_handler(state=NewBook.Name)
async def enter_name(message: Message, state: FSMContext):
    markup = await cancel_keyboard()
    name = message.text
    book = Book()
    book.name = name

    await message.answer(f'Название: {name},\n\nНапишите имя автора или нажмите "Отмена".', reply_markup=markup)
    await NewBook.Author.set()
    await state.update_data(book=book)

@dp.message_handler(state=NewBook.Author)
async def enter_name(message: Message, state: FSMContext):
    author = message.text
    data = await state.get_data()
    book: Book = data.get("book")
    book.author = author

    await message.answer(f'Автор: {author},\n\nНапишите имя Должника или /cancel.')
    await NewBook.Debtor.set()
    await state.update_data(book=book)

@dp.message_handler(state=NewBook.Debtor)
async def enter_name(message: Message, state: FSMContext):
    debtor = message.text
    data = await state.get_data()
    book: Book = data.get("book")
    book.debtor = debtor
    await book.create()

    await message.answer(f'Должник записан.')
    await state.reset_state()
    
    await message_main_menu(message)

@dp.callback_query_handler(text_contains='delete_debtor')
async def delete_debtor(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Напшите номер книги, чтобы удалить должника')
    await DeleteBook.BookID.set()

@dp.message_handler(state=DeleteBook.BookID)
async def confirm_deleting(message: Message, state:FSMContext):
    books = await get_borrowed_books()
    book_ids = []
    for num, book in enumerate(books):
        book_ids.append(book.id)
    book_id = message.text
    if int(book_id) not in book_ids:
        await message.answer('Такого id не существует.\n\nНапшите номер книги, чтобы удалить должника')
    else:
        markup = await confirm_keyboard()
        await message.answer(f'Вы хотите удалить книгу под номером {book_id}.\n\nПодтвердите действие.', reply_markup=markup)
        async with state.proxy() as data:
            data['book_id'] = book_id

        await DeleteBook.Confirm.set()

@dp.callback_query_handler(state=DeleteBook.Confirm)
async def deleting(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
            book_id = data['book_id']
    await delete_book(int(book_id))
    await call.message.answer('Должник был успешно удалён.')
    await state.reset_state()

    await call_main_menu(call)