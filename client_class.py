import socket
from time import ctime
import time
import threading
import signal
import sys

class Client:
    def __init__(self, sADDR, buff):
        self.sADDR = sADDR
        self.buff = buff
        try:
            self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.cliSock.connect(self.sADDR)
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit(1)
        self.t1 = threading.Thread(target=self.send, name=1)
        self.t2 = threading.Thread(target=self.receive, name=2)
        self.isRunning = True

    def receive(self):
        while self.isRunning:
            try:
                rMessage = self.cliSock.recv(self.buff)
                if not rMessage or rMessage.decode('utf-8') == "exit":
                    print("Ending receive connection")
                    self.stop()
                    break
                print("[{0}]: {1}".format(ctime(), rMessage.decode('utf-8')))
            except Exception as e:
                print(f"Error: {e}")
                self.stop()

    def send(self):
        while self.isRunning:
            try:
                #sMessage = input(">>")
                sMessage = "client message"
                self.cliSock.send(sMessage.encode('utf-8'))
                time.sleep(5)
                if sMessage == "exit":
                    print("Ending send connection")
                    self.stop()
                    break
            except Exception as e:
                print(f"Error: {e}")
                self.stop()

    def stop(self):
        self.isRunning = False
        self.cliSock.close()

    def close(self):
        self.stop()
        self.cliSock.close()
        print("Server closed")


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

client = Client(('localhost', 45002), 1024)

try:
    client.t1.start()
    client.t2.start()

    client.t1.join()
    client.t2.join()
except KeyboardInterrupt:
    print("Client stopped by user")

client.cliSock.close()
