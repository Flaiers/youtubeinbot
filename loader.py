from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from config import TOKEN

import logging


# уровень логов
logging.basicConfig(level=logging.INFO)

# место хранения данных FSM
storage = MemoryStorage()

# инициализация бота
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)
