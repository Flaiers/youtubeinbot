import kb

from states import Mailing
from aiogram import types
from bot import admin_id
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

# меню для админов
@dp.message_handler(user_id=admin_id, commands=['admin'])
async def admin(message: types.Message):
    await message.answer('👋 Приветствую, Admin – {0.first_name}!\n'.format(message.from_user))