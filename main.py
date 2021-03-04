import logging
import asyncio
import kb
import re

from states import Url, Lk
from config import TOKEN
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# уровень логов
logging.basicConfig(level=logging.INFO)

# место хранения данных FSM
storage = MemoryStorage()

# инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

# хэндлер на команду start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	button_youtube0 = InlineKeyboardButton('Подписаться', url='https://t.me/joinchat/R1Ct6BRjHCkO_AYO')
	inline_youtube0 = InlineKeyboardMarkup(row_width=1).add(button_youtube0)

	await message.answer('Подпишись на наш канал — Скачать Видео Ютуб в котором мы постим обновления бота и не только...!\n'
		'После подписки ты сможешь 💾 Скачать видео',
		reply_markup=inline_youtube0)
	
	await message.answer('Если подписался, перейди в Главное меню, чтобы увидеть возможности.\n'
		'PS: Нажми на кнопку внизу 👇',
		reply_markup=kb.reply_main)

# хэндлер сообщений
@dp.message_handler()
async def message(message: types.Message):
	user_channel = await bot.get_chat_member(chat_id=-1001196469736, user_id=message.from_user.id)
	if user_channel["status"] == 'left':
		"""для тех кто не подписался"""
		button_youtube1 = InlineKeyboardButton('Подписаться', url='https://t.me/joinchat/R1Ct6BRjHCkO_AYO')
		inline_youtube1 = InlineKeyboardMarkup(row_width=1).add(button_youtube1)
		await bot.send_message(message.from_user.id, 'Я проверил, ты не подписался. Подпишись 😉',
			reply_markup=inline_youtube1)

		await message.answer('Если подписался, перейди в Главное меню, чтобы увидеть возможности.\n'
			'PS: Нажми на кнопку внизу 👇',
			reply_markup=kb.reply_main)
	else:
		"""для тех кто подписался"""
		if message.text == '🏠 Главное меню':
			await message.answer('Ты находишься в Главном меню\n'
				'Чтобы скачать видео, нажми 💾 Скачать видео\n'
				'Зайти в ЛК, нажми 📰 Личный кабинет\n'
				'Есть вопрос, нажми на кнопку ниже',
				reply_markup=kb.reply_load_lk)

		elif message.text == '💾 Скачать видео':
			await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
				reply_markup=kb.reply_device_main)

		elif message.text == '📱 Приложение':
			await message.answer('Как отправить ссылку из приложения:\n'
				'Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
				'Жду ссылку от тебя)',
				reply_markup=kb.reply_back)
			await Url.app.set()

		elif message.text == '🖥 Cайт':
			await message.answer('Как отправить ссылку с сайта:\n'
				'1) Ты можешь скопировать её из адресной строки браузера и отправить мне\n'
				'2) Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
				'Жду ссылку от тебя)',
				reply_markup=kb.reply_back)
			await Url.site.set()

		elif message.text == '💻 Мобильная версия сайта':
			await message.answer('Как отправить ссылку с мобильной версии сайта:\n'
				'1) Ты можешь скопировать её из адресной строки мобильного браузера и отправить мне\n'
				'2) Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
				'Жду ссылку от тебя)',
				reply_markup=kb.reply_back)
			await Url.msite.set()

		elif message.text == '🔄 Скачать ещё раз':
			await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
				reply_markup=kb.reply_device_main)

		elif message.text == '📰 Личный кабинет':
			await message.answer('Ты зашёл в Личный кабинет, в разделе\n'
				'📚 Наши каналы можно подписаться за вознаграждение. Заработанные кристаллы можно увидеть в разделе 💎 Мои кристаллы',
				reply_markup=kb.reply_lk)
			await Lk.choice.set()

		elif message.text == '💬 Служба поддержки':
			await message.answer('⬇️ По всем вопросам сюда ⬇️\n'
				'                   t.me/Flaiers',
				reply_markup=kb.reply_main)

		elif message.text == '⬅️ Назад':
			await message.answer('Ты зашёл в Личный кабинет, в разделе\n'
				'📚 Наши каналы можно подписаться за вознаграждение. Заработанные кристаллы можно увидеть в разделе 💎 Мои кристаллы',
				reply_markup=kb.reply_lk)
			await Lk.choice.set()

		else:
			await message.answer('Я тебя не понимаю 🙃')

# хэндлер личного кабинета
@dp.message_handler(state=Lk.choice, content_types=types.ContentTypes.TEXT)
async def lk(message: types.Message, state: FSMContext):
	lk = message.text
	async with state.proxy() as data:
		data['lk1'] = lk
		choice = data['lk1']
		if choice == '💎 Мои кристаллы':
			button_sell = InlineKeyboardButton('Обмен кристаллов', callback_data='sell')
			inline_sell = InlineKeyboardMarkup(row_width=1).add(button_sell)
			try:
				user_channel = await bot.get_chat_member(chat_id=-1001269993979, user_id=message.from_user.id)
				if user_channel["status"] == 'left':
					"""для тех кто не подписался"""
					await message.answer('У тебя на счету 💳:\n'
						f'— 0 💎',
						reply_markup=inline_sell)

					await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
						reply_markup=kb.reply_back)
					await state.reset_state()

				else:
					"""для тех кто подписался"""
					await message.answer('У тебя на счету 💳:\n'
						f'— 100 💎',
						reply_markup=inline_sell)

					await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
						reply_markup=kb.reply_back)
					await state.reset_state()

			except:
				await message.answer('У тебя на счету 💳:\n'
					f'— 0 💎',
					reply_markup=inline_sell)

				await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
					reply_markup=kb.reply_back)
				await state.reset_state()

		elif choice == '📚 Наши каналы':
			await message.answer('Подписавшись на наши каналы, ты получаешь кристаллы. '
				'Эти кристаллы можно будет обменивать на различные подписки, бонусы и скидки',
				reply_markup=kb.reply_back)

			button_fla = InlineKeyboardButton('Fla.Money', url='t.me/joinchat/AAAAAEuykfvcr7wTy1J7ug')
			button_fla_check = InlineKeyboardButton('✅ Проверить', callback_data='fla_check')
			inline_fla = InlineKeyboardMarkup(row_width=2).add(button_fla, button_fla_check)
			await message.answer('Наш канал — Fla.Money в котором мы постим выигрышные исходы матчей до их начала. Так же можно купить подписку Premium, которая доступ ко всем выигрышным исходам матчей без ограничения по времени и количеству',
				reply_markup=inline_fla)

			await state.reset_state()

		elif choice == '🏠 Главное меню':
			await message.answer('Ты находишься в главном меню\n'
			'Чтобы скачать видео, нажми 💾 Скачать видео\n'
			'Зайти в ЛК, нажми 📰 Личный кабинет\n'
			'Есть вопрос, нажми на кнопку ниже',
				reply_markup=kb.reply_load_lk)
			await state.reset_state()

		else:
			await message.answer('Я тебя не понимаю 🙃')
			await state.reset_state()

# хэндлер получение от пользователя Url.app
@dp.message_handler(state=Url.app, content_types=types.ContentTypes.TEXT)
async def app(message: types.Message, state: FSMContext):
	app = message.text
	async with state.proxy() as data:
		data['app1'] = app
		answer = data['app1']
		try:
			if answer == '⬅️ Назад':
				await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
					reply_markup=kb.reply_device_main)
				await state.reset_state()

			else:
				url = answer.split('/')[3]
				button_app_720 = InlineKeyboardButton('📹 Видео 720', url=f'https://presaver.com/{url}/download/22')
				button_app_360 = InlineKeyboardButton('🎥 Видео 360', url=f'https://presaver.com/{url}/download/18')
				button_app_pic = InlineKeyboardButton('🌃 Получить превью', url=f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg')
				inline_url_app = InlineKeyboardMarkup(row_width=2).add(button_app_720, button_app_360, button_app_pic)
				await message.answer('Вот и кнопки на скачивание видеоролика\n'
					'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
					reply_markup=inline_url_app)
				await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
					reply_markup=kb.reply_r_main)
				await state.reset_state()
		except IndexError:
			await message.answer('Ты вводишь какую-то неправильную ссылку, отправь её мне снова')

# хэндлер получение от пользователя Url.site
@dp.message_handler(state=Url.site, content_types=types.ContentTypes.TEXT)
async def site(message: types.Message, state: FSMContext):
	site = message.text
	async with state.proxy() as data:
		data['site1'] = site
		answer = data['site1']
		try:
			if answer == '⬅️ Назад':
				await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
					reply_markup=kb.reply_device_main)
				await state.reset_state()

			else:
				big_url = answer.split('/')[3]
				try:
					url = big_url.split('=')[1]
					button_site_720 = InlineKeyboardButton('📹 Видео 720', url=f'https://presaver.com/{url}/download/22')
					button_site_360 = InlineKeyboardButton('🎥 Видео 360', url=f'https://presaver.com/{url}/download/18')
					button_site_pic = InlineKeyboardButton('🌃 Получить превью', url=f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg')
					inline_url_site = InlineKeyboardMarkup(row_width=2).add(button_site_720, button_site_360, button_site_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_site)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
				except:
					button_site_720 = InlineKeyboardButton('📹 Видео 720', url=f'https://presaver.com/{big_url}/download/22')
					button_site_360 = InlineKeyboardButton('🎥 Видео 360', url=f'https://presaver.com/{big_url}/download/18')
					button_site_pic = InlineKeyboardButton('🌃 Получить превью', url=f'https://i.ytimg.com/vi/{big_url}/maxresdefault.jpg')
					inline_url_site = InlineKeyboardMarkup(row_width=2).add(button_site_720, button_site_360, button_site_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_site)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
		except IndexError:
			await message.answer('Ты вводишь какую-то неправильную ссылку, отправь её мне снова')

# хэндлер получение от пользователя Url.msite
@dp.message_handler(state=Url.msite, content_types=types.ContentTypes.TEXT)
async def msite(message: types.Message, state: FSMContext):
	msite = message.text
	async with state.proxy() as data:
		data['msite1'] = msite
		answer = data['msite1']
		try:
			if answer == '⬅️ Назад':
				await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
					reply_markup=kb.reply_device_main)
				await state.reset_state()

			else:
				big_url = answer.split('/')[3]
				try:
					url = big_url.split('=')[1]
					button_msite_720 = InlineKeyboardButton('📹 Видео 720', url=f'https://presaver.com/{url}/download/22')
					button_msite_360 = InlineKeyboardButton('🎥 Видео 360', url=f'https://presaver.com/{url}/download/18')
					button_msite_pic = InlineKeyboardButton('🌃 Получить превью', url=f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg')
					inline_url_msite = InlineKeyboardMarkup(row_width=2).add(button_msite_720, button_msite_360, button_msite_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_msite)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
				except:
					button_msite_720 = InlineKeyboardButton('📹 Видео 720', url=f'https://presaver.com/{big_url}/download/22')
					button_msite_360 = InlineKeyboardButton('🎥 Видео 360', url=f'https://presaver.com/{big_url}/download/18')
					button_msite_pic = InlineKeyboardButton('🌃 Получить превью', url=f'https://i.ytimg.com/vi/{big_url}/maxresdefault.jpg')
					inline_url_msite = InlineKeyboardMarkup(row_width=2).add(button_msite_720, button_msite_360, button_msite_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_msite)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
		except IndexError:
			await message.answer('Ты вводишь какую-то неправильную ссылку, отправь её мне снова')


@dp.callback_query_handler(lambda message: message.data.startswith("fla_check"))
async def fla_check(callback_query: types.CallbackQuery, state:FSMContext):
	user_channel = await bot.get_chat_member(chat_id=-1001269993979, user_id=callback_query.from_user.id)
	if user_channel["status"] == 'left':
		"""для тех кто не подписался"""
		async with state.proxy() as data:
				fla = '0'
				data["crystal_fla"] = fla
		await bot.send_message(callback_query.from_user.id, 'Я проверил, ты не подписался. Подпишись чтобы получить кристаллы 😉',
			reply_markup=kb.reply_back)
	else:
		"""для тех кто подписался"""
		async with state.proxy() as data:
				fla = '100'
				data["crystal_fla"] = fla
		await bot.send_message(callback_query.from_user.id, 'Я проверил, ты подписался. Уже начислил тебе 100 кристаллов!\n\n'
			'Если отпишешься от канала, ты потеряешь все заработанные 💎. Нажимай Назад, чтобы вернуться в Личный кабинет',
			reply_markup=kb.reply_back)


@dp.callback_query_handler(lambda message: message.data.startswith("sell"))
async def sell(callback_query: types.CallbackQuery, state:FSMContext):
	await bot.send_message(callback_query.from_user.id, 'Недостаточно 💎 для действия. Обмен возможет только от 199, в скором времени у нас расширится база каналов и ты получишь еще больше кристаллов\n\n'
		'Если отпишешься от канала, ты потеряешь все заработанные 💎. Нажимай Назад, чтобы вернуться в Личный кабинет',
		reply_markup=kb.reply_back)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)