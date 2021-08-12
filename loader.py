import logging

from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# уровень логов
logging.basicConfig(level=logging.INFO)

# место хранения данных FSM
storage = MemoryStorage()

# инициализация бота
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)
