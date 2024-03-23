import socket
import threading


def motors(command):
    if command == "f":
        print("stop")

    elif command == "w":
        print("front")

    elif command == "d":
        print("right")

    elif command == "a":
        print("left")

    elif command == "s":
        print("back")
            

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket, client_address):
        print(f"Accepted connection from {client_address}")
        try:
            while True:
                message = client_socket.recv(1024).decode("utf-8")
                if not message:
                    print(f"Client {client_address} disconnected")
                    break
                motors(message)
                print(f"Received message from {client_address}: {message}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
        finally:
            client_socket.close()

    def start(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_handler.start()
        except KeyboardInterrupt:
            print("Server stopped by user")
        finally:
            self.server_socket.close()
            print("Server closed")

def main():
    host = "127.0.0.1"
    port = 5555
    server = Server(host, port)
    server.start()

if __name__ == "__main__":
    main()
