import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)
import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv



def commands():
    print("""command is: 
    [1] Crear una carpeta con un txt.
    """)

def doxInsert():    
    cords = input("coordenadas =>  ")
    zipz = input("zip code =>  ")
    pais =input("Country =>  ") 
    city =input("City =>  ")
    ip =input("ip =>  ")
    ig =input("instagram =>  ")
    yt = input("YouTube =>  ")
    mail = input("Email =>  ")
    dox(input("NameDox =>  "), input("Discord Nickname =>  "), input("Discord ID =>  "), input("Nombre =>  "), input("1r Apellido =>  ") , input("2nd Apellido =>  "), input("Curso => "), input("Age =>  "), input("Phone Number =>  "), input ("Address => "), cords, zipz, pais, city, ip, ig, yt, mail)


def dox(nameDox, DiscordID, Nombre, rApellido, ndApellido, Curso, Age, Instituto, PhoneNumber, Adress, Email, Youtube, Instagram, IP, City, Country, zipcode, cordenadas):

                   
    f = open(os.path.join("./Doxes","dox {0}.txt".format(nameDox)), "w", encoding="utf-8")
    f.write("""

 ▄▄▄      ▒███████▒ █    ██   ██████  ▄▄▄           ██████  ▄▄▄        █████▒▒█████  
▒████▄    ▒ ▒ ▒ ▄▀░ ██  ▓██▒▒██    ▒ ▒████▄       ▒██    ▒ ▒████▄    ▓██   ▒▒██▒  ██▒
▒██  ▀█▄  ░ ▒ ▄▀▒░ ▓██  ▒██░░ ▓██▄   ▒██  ▀█▄     ░ ▓██▄   ▒██  ▀█▄  ▒████ ░▒██░  ██▒
░██▄▄▄▄██   ▄▀▒   ░▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██      ▒   ██▒░██▄▄▄▄██ ░▓█▒  ░▒██   ██░
 ▓█   ▓██▒▒███████▒▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒   ▒██████▒▒ ▓█   ▓██▒░▒█░   ░ ████▓▒░
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░   ░ ▒░▒░▒░ 
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░   ░ ░▒  ░ ░  ▒   ▒▒ ░ ░       ░ ▒ ▒░ 
  ░   ▒   ░ ░ ░ ░ ░ ░░░ ░ ░ ░  ░  ░    ░   ▒      ░  ░  ░    ░   ▒    ░ ░   ░ ░ ░ ▒  
      ░  ░  ░ ░       ░           ░        ░  ░         ░        ░  ░           ░ ░ 
          ░ """                                                                         
"""
    \n
    Discord Nickname : {0}
    \n \n
    Discord ID : {1}
    \n \n
    Nombre : {2}
    \n \n
    1r Apellido : {3}
    \n \n
    2nd Apellido : {4}
    \n \n
    Curso : {5}
    \n \n
    Age : {6}
    \n \n
    Instituto : {7}
    \n \n
    Phone Number : {8}
    \n \n
    Address : {9}  
    \n \n
    Email : {10}
    \n \n
    Youtube : {11}
    \n \n
    instagram personal : {12}
    \n \n
    Ip : {13}
    \n \n
    City : {14}
    \n \n
    Country : {15}
    \n \n
    zip code : {16}
    \n \n
    cordenadas : {17} """.format(nameDox, DiscordID, Nombre, rApellido, ndApellido, Curso, Age, Instituto, PhoneNumber, Adress, Email, Youtube, Instagram, IP, City, Country, zipcode, cordenadas))
    
   

print(Fore.RED + """


 ▄▄▄      ▒███████▒ █    ██   ██████  ▄▄▄           ██████  ▄▄▄        █████▒▒█████  
▒████▄    ▒ ▒ ▒ ▄▀░ ██  ▓██▒▒██    ▒ ▒████▄       ▒██    ▒ ▒████▄    ▓██   ▒▒██▒  ██▒
▒██  ▀█▄  ░ ▒ ▄▀▒░ ▓██  ▒██░░ ▓██▄   ▒██  ▀█▄     ░ ▓██▄   ▒██  ▀█▄  ▒████ ░▒██░  ██▒
░██▄▄▄▄██   ▄▀▒   ░▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██      ▒   ██▒░██▄▄▄▄██ ░▓█▒  ░▒██   ██░
 ▓█   ▓██▒▒███████▒▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒   ▒██████▒▒ ▓█   ▓██▒░▒█░   ░ ████▓▒░
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░   ░ ▒░▒░▒░ 
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░   ░ ░▒  ░ ░  ▒   ▒▒ ░ ░       ░ ▒ ▒░ 
  ░   ▒   ░ ░ ░ ░ ░ ░░░ ░ ░ ░  ░  ░    ░   ▒      ░  ░  ░    ░   ▒    ░ ░   ░ ░ ░ ▒  
      ░  ░  ░ ░       ░           ░        ░  ░         ░        ░  ░           ░ ░  
          ░                                                                          
          """)

print("Dox Tool of Ghostrick | SafoSquad")

if os.path.exists('./Doxes') == False:
    directory = "Doxes"

    path1 = os.getcwd()

    path = os.path.join(path1, directory)

    os.mkdir(path)

    print("Path created in {0}".format(path))



commands()

x = True

while x == True:  
    command1 = input('root@SafoSquad =>  ')   
    
    if command1 == "1":
        doxInsert()
