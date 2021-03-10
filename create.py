from bot import key, uid
import requests

def create_link(link):
	url = f'https://bc.vc/api.php?key={key}&uid={uid}&url={link}&format=text'
	response = requests.get(url)
	create = response.text
	return create