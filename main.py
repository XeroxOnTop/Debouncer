import os, threading, json, phonenumbers, time, subprocess
from random import choice
from json import loads
from colorama import Fore
from pystyle import Anime, Colors, Center, System, Colorate
from sys import executable

"""
Date of releases : 25/11/2022
Original creator : https://github.com/XeroxOnTop
"""

System.Title("Debouncer ~ @XeroxOnTop")

requirements = [
    ["animation", "animation"],
    ["pystyle", "pystyle"],
    ["phonenumbers", "phonenumbers"]
]

for module in requirements:
    try: __import__(module[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {module[1]}", shell=True)
        time.sleep(3)

xerox = r"""

              _.===========================._
            .'`  .-  - __- - - -- --__--- -.  `'.
        __ / ,'`     _|--|_________|--|_     `'. \
      /'--| ;    _.'\ |  '         '  | /'._    ; |
     //   | |_.-' .-'.'    -  -- -    '.'-. '-._| |
    (\)   \"` _.-` /                     \ `-._ `"/
    (\)    `-`    /      .---------.      \    `-`
    (\)           |      ||1||2||3||      |
   (\)            |      ||4||5||6||      |
  (\)             |      ||7||8||9||      |
 (\)           ___|      ||*||0||#||     |
 (\)          /.--|      '---------'      |
  (\)        (\)  |\_  _  __   _   __  __/|
 (\)        (\)   |                       |
(\)_._._.__(\)    |                       |
 (\\\\\\\\\)      '.___________________.'
  '-'-'-'--'

"""[1:].replace('m','0')

Anime.Fade(text=Center.Center(xerox), color=Colors.black_to_green, mode=Colorate.Vertical, time=2)

print(Center.XCenter("Debouncer ~ @XeroxOnTop"))
print(Fore.LIGHTBLACK_EX + "[+] License : MIT License" + Fore.RESET)

def leT():
    let = input("\n\n[?] Threads : ")
    XeroxOnTop = open('config.json', 'w')
    dikt = {
    "Threads"  : f"{let}"
}
    json_string = json.dumps(dikt)
    XeroxOnTop.write(json_string)

def Main():
        while True : 

            t = "+337"+"".join(choice("3698521470") for x in range(8))
            os.makedirs("Results/",exist_ok=True)
            y = phonenumbers.parse(t)

            if phonenumbers.is_valid_number(y):
                print(f"{Fore.GREEN}[+] {Fore.RESET}" + f"Valid   : {t}")
            else: 
                print(f"{Fore.RED}[-] {Fore.RESET}" + f"Invalid : {t}")
                with open("Results/output.txt", 'a+') as file : 
                    file.write(t + '\n')
                    file.close()

check = loads(open('config.json', 'r').read())
thread = check["Threads"]

if __name__ == '__main__':
    leT()
    for b in range(int(thread)):
        th = threading.Thread(target=Main)
        th.start()
