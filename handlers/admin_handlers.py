from aiogram import Dispatcher
from aiogram.types import Message
from lexicon.lexicon import LEXICON

# Запишем ADMIN_IDS прямо в файл без всяких импортов
ADMIN_IDS = 5842666816


# Этот хэндлер будет реагировать на /start с аккаунта у которого id == ADMIN_IDS
# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# Функция для регистрации хэндлера
def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'], )  # , message.from_user=from_id
