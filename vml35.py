import requests
from bs4 import BeautifulSoup
import telebot
import time
<<<<<<< HEAD
import os
sender = telebot.TeleBot(token)
while True:
	#try:
		html = requests.get('https://vml35.ru/raspisanie-zanyatij/').text
		soup = BeautifulSoup(html, 'html.parser')
		month = ""
		date = 0
		first = 1
		document = ""
		text_to_send = ""
		for el in soup.select('.has-text-align-center'):
			txt = el.text.split()
			print(txt)
			if txt[0] == b'\xd0\x98\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'.decode():
				if date == 0:
					print('first date =', txt[-2])
					date = int(txt[-2])
					month = txt[-1]
					text_to_send = el.text
				else:
					if txt[-1] != month:
						if int(txt[-2]) < date:
							first = 0
							date = int(txt[-2])
							text_to_send = el.text
					else:
						if int(txt[-2]) > date:
							first = 0
							date = int(txt[-2])
							text_to_send = el.text
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
		mod = requests.head(document).headers['last-modified']
		if date != int(f.read()):
			sender.send_document(me, document)
			print('sended', document)
			f.close()
			f = open('last.txt', 'w')
			print(date, file=f)
		elif mod != dt.readline().strip():
			sender.send_message('@vml35', b'\xd0\xa0\xd0\xb0\xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c'.decode())
			sender.send_document('@vml35', document)
			f.close()
			dt.close()
			dt = open('dt.txt', 'w')
			f = open('last.txt', 'w')
			print(date, file=f)
			print(mod, file=dt)
		f.close()
		dt.close()
		time.sleep(60)
	#except:
		sender.send_message(me, "Error")
#sender.polling()
=======
sender = telebot.TeleBot('1001254288:AAFW0OYLAfiOVUlWR1cH07OOj3Q3B_pehJU')

while 0==0:
	html = requests.get('https://vml35.ru/raspisanie-zanyatij/').text
	soup = BeautifulSoup(html, 'html.parser')
	month = ""
	date = 0
	first = 1
	document = ""
	for el in soup.select('.has-text-align-center'):
	    txt = el.text.split()
	    print(b"0JjQt9C80LXQvdC10L3QuNGP".decode())
	    if txt[0] == b'\xd0\x98\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'.decode():
	        print(11)
	        if date == 0:
	            print(txt[-2])
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
	            print(son['href'])
	            document = son['href']
	        i += 1
	f = open('last.txt', 'r')
	print(date)
	if int(f.read()) != date:
	    #send
	    sender.send_document('@vml35', document)
	    print(document)
	    f.close()
	    f = open('last.txt', 'w')
	    print(date, file=open('last.txt', 'w'))
	sender.polling()
	time.sleep(600)
>>>>>>> parent of 3bb4d1b... WHY NOT??
	