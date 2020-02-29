import requests
from bs4 import BeautifulSoup
import telebot
import time
import os
token = os.environ['TOKEN']
me = os.environ['ME']
sender = telebot.TeleBot(token)
while True:
	try:
		html = requests.get('https://vml35.ru/raspisanie-zanyatij/').text
		soup = BeautifulSoup(html, 'html.parser')
		month = ""
		date = 0
		first = 1
		document = ""
		for el in soup.select('.has-text-align-center'):
			txt = el.text.split()
			print(txt)
			if txt[0] == b'\xd0\x98\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'.decode():
				if date == 0:
					print('first date =', txt[-2])
					date = int(txt[-2])
					month = txt[-1]
				else:
					if txt[-1] != month:
						if int(txt[-2]) < date:
							first = 0
							date = int(txt[-2])
					else:
						if int(txt[-2]) > date:
							first = 0
							date = int(txt[-2])
		i = 1
		search_for = 5 - 3*first
		for el in soup.select('.vml-tile-outer'):
			for son in el.select('.vml-tile-link'):
				if i == search_for:
					print('founded', son['href'])
					document = son['href']
				i += 1
		f = open('last.txt', 'r')
		print(date)
		if date != int(f.read()):
			sender.send_document('@vml35', document)
			print('sended', document)
			f.close()
			f = open('last.txt', 'w')
			print(date, file=f)
		f.close()
		time.sleep(60)
	except:
		sender.send_document(me, "Error")
#sender.polling()
	