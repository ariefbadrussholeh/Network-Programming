import socket
import sys
import logging

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
  while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode()

    message = str(client_socket) + " " + str(client_address) + " " + data

    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s", filemode="a")
    logging.debug(message)
    print("Receiving Data")

    client_socket.close()
    
except KeyboardInterrupt:
  server_socket.close()
  sys.exit(0)




