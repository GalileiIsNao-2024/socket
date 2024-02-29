import socket
from time import ctime
import threading

sADDR = ('localhost', 45002)
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(sADDR)

def receive():
    while True:
        rMessage = cliSock.recv(buff)
        if rMessage.decode('utf-8') == "exit":
            print("Ending connection")
            break
        print("[{0}]: {1}".format(ctime(), rMessage.decode('utf-8')))

def send():
    while True:
        sMessage = input(">>")
        cliSock.send(sMessage.encode('utf-8'))

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()

t1.join()
t2.join()