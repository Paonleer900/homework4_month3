from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

admin = [7292069375, ]
chat_id = [7292069375, ]
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
storege = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storege)
