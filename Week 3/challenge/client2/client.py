import socket
import sys

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
  while True:
    data = client_socket.recv(1024).decode()
    data = str(data).split('~')
    fileName=data[0]
    fileContain=data[1]

    print(">> Menerima file \"{}\"".format(fileName))

    with open("client2/" + fileName, "w") as file:
      file.write(fileContain)


except KeyboardInterrupt:
  client_socket.close()
  sys.exit()

