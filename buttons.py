from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

size=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='10'),
                                                   KeyboardButton(text='20'),
                                                   KeyboardButton(text='30'),
                                                   KeyboardButton(text='40'),)
