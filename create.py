# from config import key, uid
from bs4 import BeautifulSoup as bs

import requests
import logging
import urllib.request as req


def video_title(link: str) -> str:
	page_video = requests.get(f'https://www.youtube.com/watch?v={link}')
	html_video = bs(page_video.content, 'html.parser')

	title = html_video.find('title').text
	logging.info(f'\nСслыка на видео "https://www.youtube.com/watch?v={link}" — "{title}"')

	return req.pathname2url(title)


# def shorten(link):
# 	url = f'https://bc.vc/api.php?key={key}&uid={uid}&url={link}&format=text' 
# 	response = requests.get(url)
# 	create = response.text
# 	logging.info(f'Ссылка — "{link}" сокращена\n\n')
# 	return create


def video_link(url: str) -> tuple:
	name = video_title(url)

	url_720 = f'https://presaver.com/{url}/download/22?title={name}'
	url_360 = f'https://presaver.com/{url}/download/18?title={name}'
	url_image = f'https://i.ytimg.com/vi/{url}/maxresdefault.jpg'

	return url_720, url_360, url_image
