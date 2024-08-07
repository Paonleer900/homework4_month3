from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
load_dotenv()

token=getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)