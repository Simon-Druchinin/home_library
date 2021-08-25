from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def cancel_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('Отмена', callback_data='cancel')
            ]
        ]
    )

    return markup

async def show_debtors_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('Показать должников', callback_data='show_debtors')
            ],
            [
                InlineKeyboardButton('Добавить должников', callback_data='add_debtors')
            ]
        ]
    )

    return markup

async def delete_debtor_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('Добавить должника', callback_data='add_debtors')
            ],
            [
                InlineKeyboardButton('Удалить должника', callback_data='delete_debtor')
            ]
        ]
    )

    return markup

async def confirm_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('Подтвердить', callback_data='confirm')
            ],
            [
                InlineKeyboardButton('Отмена', callback_data='cancel')
            ]
        ]
    )

    return markup