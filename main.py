import socket
import threading

import rsa             #rsa was installed using pip install rsa


choice = input("Do you want to host (1) or to connect (2): ")
if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("ipv4 address", 9999))
    server.listen()


    client, _ = server.accept()

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("ipv4 address", 9999))
else:
    exit()




def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)



def receiving_messages(c):
    while True:
        message = input("")
        print("Partener: " + c.recv(1024).decode())


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
