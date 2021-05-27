from bs4 import BeautifulSoup
from bot import key, uid
import requests

def video_title(link):
	response = requests.get(link)
	soup = BeautifulSoup(response.text, 'lxml')
	title = soup.find("title").text.split(' - ')[0]
	return title

def shorten(link):
	url = f'https://bc.vc/api.php?key={key}&uid={uid}&url={link}&format=text' 
	response = requests.get(url)
	create = response.text
	return create

def video_link(type, url):
	if type == '720':
		name = video_title(url)
		link = f'https://presaver.com/{url}/download/22?title={name}'
		short = shorten(link)
		return short

	elif type == '360':
		name = video_title(url)
		link = f'https://presaver.com/{url}/download/18?title={name}'
		short = shorten(link)
		return short
	
	elif type == 'img':
		link = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'
		short = shorten(link)
		return short
