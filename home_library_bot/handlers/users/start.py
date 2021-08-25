from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.book_keyborads import show_debtors_keyboard

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    markup = await show_debtors_keyboard()
    await message.answer_photo(photo=open('files/images/books.jpg', 'rb'), caption=f"Привет, {message.from_user.full_name}!", reply_markup=markup)