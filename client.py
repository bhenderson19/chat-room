import socket
import random
import sys
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

SERVER = "127.0.0.1"
PORT = 5002
ADDR = (SERVER, PORT)
separator_token = "<SEP>" 
DISCONNECT = "!DISCONNECTED"
SHUTDOWN = "!SHUTDOWN"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def recieve_messages():
    while True:
        try:
            message = client.recv(4096).decode()
            print("\n" + message)
        except:
            pass
        
print(f"[*] Connecting...")

try:
    client.connect(ADDR)
    print("[+] Connected.")
    name = input("Enter your name: ")
    print(f"Hi {name}! Enter 'q' to exit!")

    t = Thread(target=recieve_messages)
    t.daemon = True
    t.start()

    connected = True
    while connected:
        to_send =  input()
        if to_send.lower() == 'q':
            connected = False
            to_send = DISCONNECT
        elif to_send.lower() == 'shutdown 1234':
            connected = False
            to_send = SHUTDOWN
        else:
            date_now = datetime.now().strftime('%d/%m/%Y %H:%M') 
            to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        client.send(to_send.encode())
    
except:
    print("[-] Connection failed.")
    
client.close()
sys.exit
