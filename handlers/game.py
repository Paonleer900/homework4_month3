from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

games = ['⚽️', '🎰', '🏀', '🎯', '🎳', '🎲']

async def game(message: types.Message):
    random_game=random.choice(games)
    await bot.send_dice(chat_id=message.from_user.id,emoji=random_game)


def registr_game(dp:Dispatcher):
    dp.register_message_handler(game, commands=['game'])