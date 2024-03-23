import socket

def main():
    host = "192.168.43.138"
    port = 5555

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to server")

        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message == "exit":
                break
            client_socket.send(message.encode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
