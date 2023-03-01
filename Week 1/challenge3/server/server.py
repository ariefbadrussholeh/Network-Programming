import socket
import sys

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
  while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode()

    file_name = data.split(" ")[0]
    file_data = data.split(" ")[1]
    print(file_name)
    print(file_data)
    f = open("server/" + file_name, "w")
    f.write(file_data)
    f.close()

    client_socket.close()
    
except KeyboardInterrupt:
  server_socket.close()
  sys.exit(0)




