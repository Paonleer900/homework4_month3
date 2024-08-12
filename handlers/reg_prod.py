from config import bot,dp
from aiogram import types, Dispatcher
from db import database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import size

from config import bot, dp
from aiogram import types, Dispatcher
from db import database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import size


class FSM_store(StatesGroup):
    name = State()
    sizes = State()
    category = State()
    price = State()
    photo = State()


async def reg_start(m: types.Message):
    await m.answer('name of product?')
    await FSM_store.name.set()


async def process_name(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = m.text.capitalize()
    await m.answer('size of product?', reply_markup=size)
    await FSM_store.next()

sizes=['10','20','30','40']
async def process_size(m: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    if m.text in sizes:
        async with state.proxy() as data:
            data['size'] = m.text
        await m.answer('category of product?', reply_markup=kb)
        await FSM_store.next()
    else:
        await m.answer('just press buttons!!!')


async def process_price(m: types.Message, state: FSMContext):
    if m.text.isdigit():
        async with state.proxy() as data:
            data['price'] = int(m.text)
        await m.answer('photo of product?')
        await FSM_store.next()
    else:
        await m.answer('just write numbers!!!')


async def process_category(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = m.text.capitalize()
    await m.answer('category of product?')
    await FSM_store.next()


async def process_photo(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = m.photo[-1].file_id
    await m.answer_photo(
        photo=data['photo'],
        caption=f'ur product:\n'
        f'name: {data["name"]}\n'
        f'size: {data["size"]}\n'
        f'category: {data["category"]}\n'
        f'price: {data["price"]}\n'
    )


def registr_reg_prod(dp: Dispatcher):
    dp.register_message_handler(reg_start, commands=["registration"])
    dp.register_message_handler(process_name, state=FSM_store.name)
    dp.register_message_handler(process_size, state=FSM_store.sizes)
    dp.register_message_handler(process_category, state=FSM_store.category)
    dp.register_message_handler(process_price, state=FSM_store.price)
    dp.register_message_handler(process_photo, state=FSM_store.photo,content_types='photo')