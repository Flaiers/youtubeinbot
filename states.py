from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):

	video = State()
	choice = State()
