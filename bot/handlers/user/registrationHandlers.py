from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states.registrationStates import Registration
from keyboards.default.basicKeyboards import ask_number, age_list, courseButtons
from data.gSheets import write_to_google_sheets
import re
from loader import dp, db



@dp.message(Command("register"))
async def handle_registration(message: Message, state: FSMContext):
    await message.answer("Ismingiz va familiyangizni kiriting 📄:")
    await state.set_state(Registration.name)


@dp.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Telefon raqamingizni yuboring 📞👇:", reply_markup=ask_number)
    await state.set_state(Registration.phone)

@dp.message(Registration.phone)
async def process_phone(message: Message, state: FSMContext):
    phone_regex = re.compile(r'^\+998[0-9]{9}$')
    if message.contact:
        number = message.contact.phone_number
        await state.update_data(phone=number)
    else:
        number = message.text
        if bool(phone_regex.match(number)):
            await state.update_data(phone=number)
        else:
            await message.answer("Telefon raqam formati to'g'ri emas❌.\nTelefon raqamingizni kiriting yoki tugma orqali raqamingizni yuboring.")
            await state.set_state(Registration.phone)
            return
    await message.answer("Yoshingizni tanlang:", reply_markup=age_list)
    await state.set_state(Registration.age)

@dp.message(Registration.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("💻 Quyidagi kurslardan birini tanlang:", reply_markup=courseButtons)
    await state.set_state(Registration.course)



@dp.message(Registration.course)
async def process_course(message: Message, state: FSMContext):
    courses = ["💻 Kompyuter savodxonligi", "📲 Android", "🌐 Backend", "🖥️ Frontend", "🎨 Grafik dizayn"]
    course = message.text
    if course not in courses:
        await message.answer("💻 Kurslardan birini tanlang:", reply_markup=courseButtons)
        return
    await state.update_data(course=course)
    data = await state.get_data()
    write_to_google_sheets([
        message.from_user.id,
        data["name"],
        data["age"],
        data["phone"],
        data["course"]
    ])
    db.new_user(
        id=message.from_user.id,
        name=data["name"],
        phone=data["phone"],
        age=data["age"],
        course=data["course"]
    )
    await message.answer("24 soat 🕗 ichida xodimlarimiz siz bilan bog'lanishadi.✅")
    await state.clear()

