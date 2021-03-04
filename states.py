from aiogram.dispatcher.filters.state import StatesGroup, State

class Url(StatesGroup):
	app = State()
	site = State()
	msite = State()

class Lk(StatesGroup):
	choice = State()

class Mailing(StatesGroup):
    text = State()