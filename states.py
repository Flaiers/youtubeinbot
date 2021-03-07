from aiogram.dispatcher.filters.state import StatesGroup, State

class Save(StatesGroup):
	video = State()

class Lk(StatesGroup):
	choice = State()

class Mailing(StatesGroup):
    text = State()