from bot import api
import requests

def create_link(link):
	url = f"https://shrlink.top/api?api={api}&url={link}&format=text"
	response = requests.get(url)
	create = response.text
	return create