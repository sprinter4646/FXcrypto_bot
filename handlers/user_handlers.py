from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from lexicon.lexicon import LEXICON
from keyboards.user_kb import start_kb, choose_cur
from services.FXrates_handling import FXrates_db, FXrates_db_print
from aiogram import types


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=start_kb)


# Этот хэндлер срабатывает на нажатие пользователем кнопки 'Выберите валютную пару'
async def process_choose_cur(message: Message):
    await message.answer(text=LEXICON['cur_btn'], reply_markup=choose_cur)


# Этот хэндлер срабатывает на кнопку с любой валютной парой
async def process_any_cur_btn(message: Message):
    await message.answer(f'{FXrates_db_print(message.text)}', parse_mode=types.ParseMode.HTML)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_choose_cur,
                                text=LEXICON['cur_btn'])
    dp.register_message_handler(process_any_cur_btn,
                                Text(equals=[LEXICON['RUB/USD_btn'],
                                             LEXICON['USDT/USD_btn'],
                                             LEXICON['THB/USD_btn'],
                                             LEXICON['RUB/THB_btn']]))
