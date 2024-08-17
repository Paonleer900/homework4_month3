from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

admin = [123456789, 987654321]


TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
storege = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storege)
