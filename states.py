from aiogram.dispatcher.filters.state import StatesGroup, State

class Save(StatesGroup):
	app = State()
	site = State()
	msite = State()

class Lk(StatesGroup):
	choice = State()

class Mailing(StatesGroup):
    text = State()