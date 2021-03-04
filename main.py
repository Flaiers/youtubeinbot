import random, kb, asyncio, re

from bot import unknown
from aiogram import types
from create import create_link
from states import Lk, Url, Mailing
from loader import dp, bot, storage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# хэндлер на команду start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	button_youtube0 = InlineKeyboardButton('Подписаться', url='t.me/joinchat/R1Ct6BRjHCkO_AYO')
	inline_youtube0 = InlineKeyboardMarkup(row_width=1).add(button_youtube0)

	await message.answer('Подпишись на наш канал — Скачать Видео Ютуб в котором мы постим обновления бота, выкладываем интеремную информацию в сфере IT, а также устраиваем розыгрыши!\n\n'
		'Мы будем очень благодарны тебе 🥰',
		reply_markup=inline_youtube0)
	
	await message.answer('Перейди в Главное меню, чтобы Скачать видео\n'
		'PS: Нажми на кнопку внизу 👇',
		reply_markup=kb.reply_main)

# хэндлер сообщений
@dp.message_handler()
async def message(message: types.Message):
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
		await message.answer(random.choice(unknown),
			reply_markup=kb.reply_load_lk)

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
				user_channel = await bot.get_chat_member(chat_id=-1001196469736, user_id=message.from_user.id)
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

			button_fla = InlineKeyboardButton('Скачать Видео Ютуб', url='t.me/joinchat/R1Ct6BRjHCkO_AYO')
			button_fla_check = InlineKeyboardButton('✅ Проверить', callback_data='fla_check')
			inline_fla = InlineKeyboardMarkup(row_width=2).add(button_fla, button_fla_check)
			await message.answer('Наш канал — Скачать Видео Ютуб в котором мы постим обновления бота, выкладываем интеремную информацию в сфере IT, а также устраиваем розыгрыши!',
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
			await message.answer(random.choice(unknown),
				reply_markup=kb.reply_lk)

			await state.reset_state()
			await Lk.choice.set()

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
				link_720 = f'https://presaver.com/{url}/download/22'
				link_360 = f'https://presaver.com/{url}/download/18'
				link_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
				url_720 = create_link(link_720)
				url_360 = create_link(link_360)
				url_image = create_link(link_image)
				button_app_720 = InlineKeyboardButton('📹 Видео 720', url=url_720)
				button_app_360 = InlineKeyboardButton('🎥 Видео 360', url=url_360)
				button_app_pic = InlineKeyboardButton('🌃 Получить превью', url=url_image)
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
					link_720 = f'https://presaver.com/{url}/download/22'
					link_360 = f'https://presaver.com/{url}/download/18'
					link_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
					url_720 = create_link(link_720)
					url_360 = create_link(link_360)
					url_image = create_link(link_image)
					button_site_720 = InlineKeyboardButton('📹 Видео 720', url=url_720)
					button_site_360 = InlineKeyboardButton('🎥 Видео 360', url=url_360)
					button_site_pic = InlineKeyboardButton('🌃 Получить превью', url=url_image)
					inline_url_site = InlineKeyboardMarkup(row_width=2).add(button_site_720, button_site_360, button_site_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_site)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
				except:
					link_720 = f'https://presaver.com/{url}/download/22'
					link_360 = f'https://presaver.com/{url}/download/18'
					link_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
					url_720 = create_link(link_720)
					url_360 = create_link(link_360)
					url_image = create_link(link_image)
					button_site_720 = InlineKeyboardButton('📹 Видео 720', url=url_720)
					button_site_360 = InlineKeyboardButton('🎥 Видео 360', url=url_360)
					button_site_pic = InlineKeyboardButton('🌃 Получить превью', url=url_image)
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
					link_720 = f'https://presaver.com/{url}/download/22'
					link_360 = f'https://presaver.com/{url}/download/18'
					link_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
					url_720 = create_link(link_720)
					url_360 = create_link(link_360)
					url_image = create_link(link_image)
					button_msite_720 = InlineKeyboardButton('📹 Видео 720', url=url_720)
					button_msite_360 = InlineKeyboardButton('🎥 Видео 360', url=url_360)
					button_msite_pic = InlineKeyboardButton('🌃 Получить превью', url=url_image)
					inline_url_msite = InlineKeyboardMarkup(row_width=2).add(button_msite_720, button_msite_360, button_msite_pic)
					inline_url_msite = InlineKeyboardMarkup(row_width=2).add(button_msite_720, button_msite_360, button_msite_pic)
					await message.answer('Вот и кнопки на скачивание видеоролика\n'
						'Кликай на ту кнопку соответственно которой хочешь разрешение видеоролика:',
						reply_markup=inline_url_msite)
					await message.answer('Теперь ты можешь ещё раз скачать видеоролик, или вернуться в Главное меню',
						reply_markup=kb.reply_r_main)
					await state.reset_state()
				except:
					link_720 = f'https://presaver.com/{url}/download/22'
					link_360 = f'https://presaver.com/{url}/download/18'
					link_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
					url_720 = create_link(link_720)
					url_360 = create_link(link_360)
					url_image = create_link(link_image)
					button_msite_720 = InlineKeyboardButton('📹 Видео 720', url=url_720)
					button_msite_360 = InlineKeyboardButton('🎥 Видео 360', url=url_360)
					button_msite_pic = InlineKeyboardButton('🌃 Получить превью', url=url_image)
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
	user_channel = await bot.get_chat_member(chat_id=-1001196469736, user_id=callback_query.from_user.id)
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