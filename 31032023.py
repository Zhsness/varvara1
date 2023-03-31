import sqlite3
import threading
import time
import requests
from bs4 import BeautifulSoup as bs



a = []

def parse12345(lst):
  for i in lst:
    soup = bs(i, 'html.parser')
    res = soup.find_all("description")
    for j in res:
        print(j.getText())


def main(link):
    response = requests.get(link)   
    a.append(response.text)


   
c1 = time.time()

t1 = threading.Thread(target = main, args = ("http://lenta.ru/rss/news", ))
t1.start()


t1.join()

parse12345 (a)

print(time.time() - c1)