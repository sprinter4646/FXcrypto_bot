from aiogram import Dispatcher
from aiogram.types import Message


# Этот хэндлер будет реагировать на любые текстовые сообщения пользователя
async def send_echo(message: Message):
    print(f'Message отправлено с аккаунта имеющего id = {message.from_id}')  # Печатаем id аккаунта
    await message.answer(f'Это эхо! {message.text}')


# Функция для регистрации хэндлера
def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)
    