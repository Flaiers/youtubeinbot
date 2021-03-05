from bot import admin_id, api_id, api_hash, name
from aiogram import executor
from datetime import datetime
from loader import dp, bot, storage
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

async def get_user(id):
	async with TelegramClient(name, api_id, api_hash) as client:
		await client.start()
		username = await client(GetFullUserRequest(id))
		return username.user.first_name

async def on_startup(dp):
	username = await get_user(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y %T')
	await bot.send_message(admin_id, f'Привет, {username}!\nЯ запущен!\nСейчас: ' + time)

async def on_shutdown(dp):
	username = await get_user(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y %T')
	await bot.send_message(admin_id, f'Пока, {username}!\nЯ остановлен!\nСейчас: ' + time)
	await bot.close()
	await storage.close()


if __name__ == '__main__':
	from admin import dp
	from handlers import dp

	executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)