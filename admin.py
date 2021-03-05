import kb

from states import Mailing
from aiogram import types
from bot import admin_id
from loader import dp, bot, storage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

# меню для админов
@dp.message_handler(user_id=admin_id, commands=['admin'])
async def admin(message: types.Message):
    await message.answer('👋 Приветствую, Admin – {0.first_name}!'
        '\n/mailing – произвести рассылку сообщения всем пользователям бота'.format(message.from_user),
        reply_markup=kb.reply_menu_admin)

# Рассылка по юзерам
@dp.message_handler(user_id=admin_id, commands=['mailing'])
async def mailing(message: types.Message):
    await message.answer('Пришлите текст рассылки')
    await Mailing.text.set()

@dp.callback_query_handler(user_id=admin_id, state=Mailing.text)
async def mailing_start(message: types.Message, state: FSMContext):
    text = message.text
    async with state.proxy() as data:
        data['text1'] = text
        mail = data['text1']