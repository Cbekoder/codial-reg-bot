from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import html
from loader import dp, db

from states.registrationStates import Registration


@dp.message(CommandStart())
async def command_start_handler(message: Message, state=FSMContext) -> None:
    if len(message.text.split()) > 1:
        args = message.text.split()[1]
    else:
        args = None

    if args == "register" or not db.select_user(message.from_user.id):
        await message.answer(f"Assalomu alaykum, {html.bold(message.from_user.full_name)}\nCodial zamonaviy kasblar akademiyasining botiga xush kelibsiz.\n\n"
                             f"Kurslarimizdan ro'yxatdan o'tish uchun \nismingiz va familiyangizni kiriting✍️:")
        await state.set_state(Registration.name)
    else:
        await message.answer(f"Assalomu alaykum, {html.bold(message.from_user.full_name)}\nCodial zamonaviy kasblar akademiyasining botiga xush kelibsiz.\n\n"
                             f"📋Kurslarimizdan ro'yxatdan o'tish uchun /register buyrug'idan foydalaning!")
        await state.clear()
