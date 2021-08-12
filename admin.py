from aiogram import types
from config import admin_id
from loader import dp


# функции для админов
@dp.message_handler(user_id=admin_id, commands=['admin'])
async def admin(message: types.Message):
    await message.answer('👋 Приветствую, Admin – {0.first_name}!\n'.format(message.from_user))
