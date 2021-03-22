from bot import key
import requests

def create_link(link):
	url = f'http://q32.link/api.php?key={key}&url={link}&format=text'
	response = requests.get(url)
	create = response.text
	return create