from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons


class FSM_reg(StatesGroup):
    fullname = State()
    age = State()
    email = State()
    gender = State()
    phone = State()
    photo = State()


async def fsm_start(message: types.Message):
    await message.answer(text='Привет! \n'
                              'Напиши своё фио:\n\n'
                              '!Для того чтобы воспользоваться командами, '
                              'нажмите на "Отмена"!', reply_markup=buttons.cancel)
    await FSM_reg.fullname.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await FSM_reg.next()
    await message.answer(text='Укажите свой возрас:т')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await FSM_reg.next()
    await message.answer(text='Укажите свою почту:')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!')


def register_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_start, commands=['registration'])
    dp.register_message_handler(load_name, state=FSM_reg.fullname)
    dp.register_message_handler(load_age, state=FSM_reg.age)
