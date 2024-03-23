import socket
import keyboard

global_key = ""

def changeKey(key):
    global global_key
    if key == 'w' or key == 'a' or key == 's' or key == 'd' or key == 'f':
        global_key = key
    else:
        global_key = "f"

keyboard.on_press_key("w", lambda _: changeKey('w'))
keyboard.on_press_key("a", lambda _: changeKey('a'))
keyboard.on_press_key("s", lambda _: changeKey('s'))
keyboard.on_press_key("d", lambda _: changeKey('d'))
keyboard.on_press_key("f", lambda _: changeKey('f'))


def main():
    global global_key
    old_key = ""
    host = "192.168.43.138"
    port = 5557

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to server")

        while True:
            if old_key != global_key:
                message = global_key
                if message == "exit":
                    break
                client_socket.send(message.encode("utf-8"))
                old_key = global_key

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
