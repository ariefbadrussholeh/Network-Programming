import socket
import sys
import logging
from datetime import datetime

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
  while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode()

    message = str(client_address) + " " + data
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s", filemode="a")
    logging.debug(message)
    print("Receiving Data")

    if (data == "asklog"):
      datasend = open("log.txt", "r").read()
      
    else:
      datasend = str(datetime.now()) + " " + str(client_address) + " " + data
    
    print("Sending Data")
    client_socket.send(datasend.encode())

    client_socket.close()
    
except KeyboardInterrupt:
  server_socket.close()
  sys.exit(0)




