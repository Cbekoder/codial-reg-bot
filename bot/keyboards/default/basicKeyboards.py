from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ask_number = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamimni ulashish☎️", request_contact=True),
        ]
    ]
)


age_list = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='18-20'),
            KeyboardButton(text='21-24'),
            KeyboardButton(text='25+')
        ]
    ]
)

courseButtons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="💻 Kompyuter savodxonligi"),
            KeyboardButton(text="📲 Android"),
        ],
        [
            KeyboardButton(text="🌐 Backend"),
            KeyboardButton(text="🖥️ Frontend"),
            KeyboardButton(text="🎨 Grafik dizayn")
        ]
    ]
)
