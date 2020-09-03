#coding=utf-8
import requests, os, sys, urllib.request, time, threading
from bs4 import BeautifulSoup
from time import sleep
_r = '\033[1;31m'
_h = '\033[1;32m'
_k = '\033[1;33m'
_p = '\033[1;0m'
session = requests.Session()
stop_dl = None


def logo():
	os.system("clear")
	print(_r+"="*42)
	print("Author : Safar")
	print(_k+"Support : Tekat")
	print("Team : XiuzCode")
	print(_h+"Tool : Downloader Mp3")
	print(_r+"___  ____ _ _ _ _  _ _    ____ ____ ___  ")
	print(_k+"|  \ |  | | | | |\ | |    |  | |__| |  \ ")
	print(_h+"|__/ |__| |_|_| | \| |___ |__| |  | |__/ ")
	print(_r+"="*42)
	pk = input(_p+"TEKAN ENTER UNTUK LANJUT... ")

def menu():
    global stop_dl
    stop_dl = False
    logo()
    url = "https://downloadlagu321.net"
    konten = session.get(url)
    soup = BeautifulSoup(konten.content, "html.parser")
    angka = -1
    data = []
    for lagu in soup.find_all(class_="info-name"):
        angka += 1
        print (str([angka]),lagu.text)#,lagu["href"])
        for jud in lagu.findChildren("a"):
               data.append([jud.text,jud.get('href')])
               break
    inp = int(input("[+] Pilih : "))
    res2 = session.get(data[inp][1])
    soup = BeautifulSoup(res2.content, "html.parser")
    angka = -1
    daa = []
    for lagu in soup.find_all(class_="button-download"):
        res3 = session.get(lagu["href"])
        soup = BeautifulSoup(res3.content, "html.parser")
        for x in soup.find_all(rel="nofollow noopener noreferrer"):
            daa.append([x.text,x["href"]])
    inp = 0
    da = daa[inp][1]
    ak = input("nama mp3 : ")
    threading.Thread(target=download, args=(da, ak+'.mp3')).start()
    if not stop_dl:
      for x in ["\\","-","/","-"]:
        print("\r downloading %s ... %s" % (ak+'.mp3', x), end="")
    print("\nselesai download di simpan di %s " % (ak+'.mp3'))
def download(url, filenama):
    with open(filenama, "wb") as f:
         res = requests.get(url).content
         f.write(res)
    stop_dl = True

menu()
