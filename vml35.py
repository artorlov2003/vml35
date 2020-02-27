import requests
from bs4 import BeautifulSoup
import telebot
import time
sender = telebot.TeleBot('1001254288:AAFW0OYLAfiOVUlWR1cH07OOj3Q3B_pehJU')


html = requests.get('https://vml35.ru/raspisanie-zanyatij/').text
soup = BeautifulSoup(html, 'html.parser')
month = ""
date = 0
first = 1
document = ""
for el in soup.select('.has-text-align-center'):
    txt = el.text.split()
    print(txt)
    if txt[0] == b"0JjQt9C80LXQvdC10L3QuNGP".decode():
        if date == 0:
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


i = 0
search_for = 5 - 3*first
for el in soup.select('.vml-tile-outer'):
    for son in el.select('.vml-tile-link'):
        if i == search_for:
            print(son['href'])
            document = son['href']
        i += 1
f = open('last.txt', 'r')
if int(f.read()) != date:
    #send
    sender.send_document('@vml35', document)
    print(document)
    f.close()
    f = open('last.txt', 'w')
    print(date, file=open('last.txt', 'w'))
sender.polling()
time.sleep(600)
