import socket
from time import ctime
import threading
import signal
import sys

class Server:
    def __init__(self, sADDR, buff):
        self.sADDR = sADDR
        self.buff = buff
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servSock.bind(self.sADDR)
        self.servSock.listen(5)

    def start(self):
        while True:
            print("Waiting for a connection...")
            self.cliSock, self.cADDR = self.servSock.accept()
            print("...Connection made with {0}".format(self.cADDR))
            self.t1 = threading.Thread(target=self.send, name=3)
            self.t2 = threading.Thread(target=self.receive, name=4)
            self.isRunning = True
            self.t1.start()
            self.t2.start()
            self.t1.join()
            self.t2.join()
            self.cliSock.close()

    def receive(self):
        while self.isRunning:
            rMessage = self.cliSock.recv(self.buff)
            if not rMessage or rMessage.decode('utf-8') == "exit":
                print("Ending connection")
                self.stop()
                break
            print("[{0}]: {1}".format(ctime(), rMessage.decode('utf-8')))

    def send(self):
        while self.isRunning:
            sMessage = input(">>")
            if not sMessage:
                break
            self.cliSock.send(sMessage.encode('utf-8'))

    def stop(self):
        self.isRunning = False
    
    def close(self):
        self.stop()
        self.servSock.close()
        print("Server closed")


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

server = Server(("", 45002), 1024)
server.start()
