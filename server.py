import socket
import sys
from threading import Thread

from sendemail import send_email

SERVER = "0.0.0.0"
PORT = 5002
ADDR = (SERVER, PORT)
separator_token = "<SEP>"
DISCONNECT = "!DISCONNECTED"
SHUTDOWN = "!SHUTDOWN"

client_sockets = set()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[+] {addr} connected.")
    client_sockets.add(conn)
    connected=True

    joinMsg = f"A user has joined. There are {len(client_sockets)-1} other clients connected"
    send_email("A user has joined. There are "+str(len(client_sockets))+" other clients connected")
    for client_socket in client_sockets:
        try:
            client_socket.send(joinMsg.encode())
        except:
            connected = False

    while connected:
        try:
            msg = conn.recv(4096).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            send_email("[!] Error: "+e)
            connected = False
        if msg == DISCONNECT:
            connected = False
        elif msg == SHUTDOWN:
            print("[v] Server shutting down...")
            send_email("[v] Server shutting down...")
            stop()
        else:
            msg = msg.replace(separator_token, ": ")
            for client_socket in client_sockets:
                try:
                    client_socket.send(msg.encode())
                except:
                    connected = False

    print(f"[-] {addr} disconnected.")
    client_sockets.remove(conn)
    leftMsg = f"A user has disconnected. There are {len(client_sockets)-1} other clients connected"
    send_email("A user has disconnected. There are "+str(len(client_sockets))+" other clients connected")
    try:
        for client_socket in client_sockets:
            try:
                client_socket.send(leftMsg.encode())
            except:
                pass
    except:
        pass
    conn.close()
    
def stop():
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    sys.exit

def start():
    print(f"[*] Listening as {SERVER}:{PORT}")
    server.listen()
    while True:
        conn,addr = server.accept()
        t = Thread(target=handle_client,args=(conn,addr))
        t.daemon = True
        t.start()

print("[^] Server is starting...")
send_email("[^] Server is starting...")
try:
    start()
except:
    sys.exit