from bot import key, uid
import requests, urllib.request as req
import pytube

def video_title(link):
	video = pytube.YouTube(f'https://www.youtube.com/watch?v={link}')
	return req.pathname2url(video.title)

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
