import requests as r
from bs4 import BeautifulSoup as fuck
import urllib,time,sys,os
from time import sleep

hed = {
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
}
logo = """#Author : Safar              #
#Support : My Team           #
#Team : From XiuzCode        #
#Tool : Downloader           #
#My Contact : +6282288231535 #"""
def menu():
	os.system("clear")
	print("="*30)
	print(logo)
	print("="*30)
	print("########[ DOWNLOADER ]########")
	print("1.Download Lagu Youtube      #")
	print("2.Download Video Youtube     #")
	print("="*30)
	anjing = input("Pilih No : ")
	if anjing=="1":
		tes()
	elif anjing=="2":
		tes1()
	else:
		print("Masukan Angkanya anjing.... ")
		sleep(2)
		menu()

def tes():
	c = input("Link : ")
	s = c.replace("https://youtu.be/","")
	daa = {
	"type":"youtube",
	"_id":"5e9e0b5f7527f8446a8b45ad",
	"v_id":s,
	"ajax":"1",
	"ftype":"mp3",
	"fquality":"128"
	}
	
	b = r.post("https://mate09.y2mate.com/id/convert/",data=daa,headers=hed)
	soup = fuck(b.content, 'html.parser')
	for x in soup.find_all("a"):
		b = x["href"]
		f = b.replace('"',"").replace(f"\\","")
		#print(f)
		kontol = input("Buat nama lagu : ")
		print("Nama Lagu : ",kontol+'.mp3') 
		urllib.request.urlretrieve(f,kontol+'.mp3',reporthook=Download_Progress)

def Download_Progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def tes1():
	c = input("Link : ")
	s = c.replace("https://youtu.be/","")
	daa = {
	"type":"youtube",
	"_id":"5e9e0b5f7527f8446a8b45ad",
	"v_id":s,
	"ajax":"1",
	"ftype":"mp4",
	"fquality":"360"
	}

	b = r.post("https://mate09.y2mate.com/id/convert/",data=daa,headers=hed)
	#print(b)
	soup = fuck(b.content, 'html.parser')
	for tx in soup.find_all("a"):
		b = tx["href"]
		f = b.replace('"',"").replace(f"\\","")
		kontol = input("Buat nama video : ")
		print("Nama Video : ",kontol+'.mp4') 
		urllib.request.urlretrieve(f,kontol+'.mp4',reporthook=Download_Progress)
		


menu()

