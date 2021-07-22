from bot import key, uid
from bs4 import BeautifulSoup as bs

import requests, logging, urllib.request as req


def video_title(link):
	page_video = requests.get(f'https://www.youtube.com/watch?v={link}')
	html_video = bs(page_video.content, 'html.parser')
	title = html_video.find('title').text
	logging.info(f'Название видео "{link}" — "{title}"\n\n')
	return req.pathname2url(title)

def shorten(link):
	url = f'https://bc.vc/api.php?key={key}&uid={uid}&url={link}&format=text' 
	response = requests.get(url)
	create = response.text
	logging.info(f'Ссылка — "{link}" сокращена\n\n')
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
