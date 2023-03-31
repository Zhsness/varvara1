import sqlite3
import threading
import time
import requests


def main(a, b):
  response = requests.get(a)
  #print(response.text)
  file = open(f"C:/Users/Stud2/Documents/29032023/{b}moon.jpg", mode = "wb")
  file.write(response.content)
  file.close()
  #print("file created")
 

t1 = threading.Thread(target = main , args = ("https://images.squarespace-cdn.com/content/v1/52c1f91ee4b0a77a50337e61/1531670822250-F0WEQX7OT906NBGPXZB2/moon.jpg","test"))
t1.start()



t1 = threading.Thread(target = main , args = ("https://i.ytimg.com/vi/lcXsunmdAKo/maxresdefault.jpg","test1"))
t1.start()

t1 = threading.Thread(target = main , args = ("https://www.belta.by/images/storage/news/with_archive/2022/000029_1650378973_497091_big.jpg", "test2"))
t1.start()

t1 = threading.Thread(target = main , args = ("https://img.freepik.com/vector-gratis/lindo-sol-sonriente-vector-elemento-diseno-etiqueta-nubes_53876-164996.jpg", "test3"))
t1.start()