import socket
import sys
import threading

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

def receive_data():
    while True:
        data = client_socket.recv(1024).decode()
        data = str(data).split('~')
        fileName=data[0]
        fileContain=data[1]

        with open("client3/" + fileName, "w") as file:
          file.write(fileContain)

def user_input():
    while True:
        fileName = input(">> ")
        with open("client3/" + fileName, 'r') as file:
          fileContent = file.read()

        message = "{}~{}".format(fileName, fileContent)

        client_socket.send(message.encode())

t1 = threading.Thread(target=receive_data)
t2 = threading.Thread(target=user_input)

t1.start()
t2.start()

