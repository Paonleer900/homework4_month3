from config import bot,dp
from aiogram import types, Dispatcher



async def send_files(message: types.Message):
    await bot.send_document(
        chat_id==message.fron_user.id,
        document=open('config.py', 'rb')
    )




def register_file(dp:Dispatcher):
    dp.register_message_handler(send_files, commands=['file'])