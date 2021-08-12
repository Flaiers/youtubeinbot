import kb

from config import admin_id, api_id, api_hash, name
from aiogram import executor
from datetime import datetime
from time import sleep
from loader import bot, storage
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest


async def get_user_id(id):
	async with TelegramClient(name, api_id, api_hash) as client:
		await client.start()
		username = await client(GetFullUserRequest(id))
		return username.user.first_name


async def on_startup(dp):
	username = await get_user_id(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y в %T UTC')
	sleep(5)
	await bot.send_message(admin_id, f'Привет, {username}!\nЗапущен {time}')


async def on_shutdown(dp):
	username = await get_user_id(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y в %T UTC')
	sleep(5)
	await bot.send_message(
		admin_id,
		f'Пока, {username}!\nОстановлен {time}',
		reply_markup=kb.reply_remove
	)
	await bot.close()
	await storage.close()

if __name__ == '__main__':
	from admin import dp
	from handlers import dp

	executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
