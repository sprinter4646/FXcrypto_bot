from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon import LEXICON

# Создаем клавиатуру с кнопкой "Выберите валютную пару"
start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True)

cur_btn: KeyboardButton = KeyboardButton(LEXICON['cur_btn'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
start_kb.add(cur_btn)

# Создаем клавиатуру с кнопками выбора валютных пар
choose_cur: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                      resize_keyboard=True)

button_1: KeyboardButton = KeyboardButton(LEXICON['RUB/USD_btn'])
button_2: KeyboardButton = KeyboardButton(LEXICON['USDT/USD_btn'])
button_3: KeyboardButton = KeyboardButton(LEXICON['THB/USD_btn'])
button_4: KeyboardButton = KeyboardButton(LEXICON['RUB/THB_btn'])

# Располагаем кнопки в клавиатуре одну под другой в 4 ряда
choose_cur.add(button_1).add(button_2).add(button_3).add(button_4)
