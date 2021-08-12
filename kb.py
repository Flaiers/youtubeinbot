from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
							ReplyKeyboardRemove

# текст кнопок
button_main = KeyboardButton('🏠 Главное меню')
button_load = KeyboardButton('💾 Скачать видео')
button_r = KeyboardButton('🔄 Скачать ещё раз')
button_lk = KeyboardButton('📰 Личный кабинет')
button_p = KeyboardButton('💎 Мои кристаллы')
button_cl = KeyboardButton('📚 Наши каналы')
button_help = KeyboardButton('💬 Служба поддержки')
button_back = KeyboardButton('⬅️ Назад')
button_app = KeyboardButton('📱 Приложение')
button_site = KeyboardButton('🖥 Cайт')
button_msite = KeyboardButton('💻 Мобильная версия сайта')

# включение в работу кнопок
reply_main = ReplyKeyboardMarkup(resize_keyboard=True).add(button_main)

reply_r_main = ReplyKeyboardMarkup(resize_keyboard=True) \
			.add(button_r).add(button_main)

reply_lk = ReplyKeyboardMarkup(resize_keyboard=True) \
			.add(button_p).add(button_cl).add(button_main)

reply_menu = ReplyKeyboardMarkup(resize_keyboard=True) \
			.add(button_load).add(button_lk).add(button_help)

reply_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)

reply_device = ReplyKeyboardMarkup(resize_keyboard=True) \
			.add(button_app, button_site).add(button_msite).add(button_main)

reply_remove = ReplyKeyboardRemove()
