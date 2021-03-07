from bot import admin_id, api_id, api_hash, name
from aiogram import executor
from datetime import datetime
from loader import dp, bot, storage
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import pymyip, kb

async def get_user_id(id):
	async with TelegramClient(name, api_id, api_hash) as client:
		await client.start()
		username = await client(GetFullUserRequest(id))
		return username.user.first_name

async def on_startup(dp):
	ip = pymyip.get_ip()
	city = pymyip.get_city()
	country = pymyip.get_country()
	username = await get_user_id(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y в %T UTC')
	await bot.send_message(admin_id, f'Привет, {username}!\nЗапущен {time}\nМесто запуска: {city}, {country} (IP = {ip})')

async def on_shutdown(dp):
	ip = pymyip.get_ip()
	city = pymyip.get_city()
	country = pymyip.get_country()
	username = await get_user_id(admin_id)
	now = datetime.now()
	time = now.strftime('%d/%m/%y в %T UTC')
	await bot.send_message(admin_id, f'Пока, {username}!\nОстановлен {time}\nМесто остановки: {city}, {country} (IP = {ip})',
		reply_markup=kb.reply_remove)
	await bot.close()
	await storage.close()

if __name__ == '__main__':
	from admin import dp
	from handlers import dp

	executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)