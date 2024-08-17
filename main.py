import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, echo, quiz, FSM_reg, FSM_online_store, notification, send_products
from db import db_main
from aiogram import types
from aiogram import Bot, Dispatcher
from handlers import notification



admin = [7292069375, ]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot on')
        await db_main.sql_create()



async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot off')
        await db_main.sql_create()




commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_reg.register_fsm(dp)
FSM_online_store.store_fsm(dp)
notification.register_notification(dp)
send_products.register_send_products_handler(dp)

echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)