import socket
import select
import sys

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

def isPalindrome(s):
  return s == s[::-1]

try:
  while True:
    read_ready, write_ready, exception = select.select(input_socket, [], [])

    for sock in read_ready:
      if sock == server_socket:
        client_socket, client_address = server_socket.accept()
        input_socket.append(client_socket)
      else:
        data = sock.recv(1024).decode()

        lines = data.split('\n')

        with open("server/temp.txt", "w") as file:
          file.write("")

        for line in lines:
          with open("server/temp.txt", 'a') as file:
            if line == "":
              break
            elif(isPalindrome(line.replace('\n', ''))):
              file.write(line.replace('\n', '') + " - yes\n")
            else:
              file.write(line.replace('\n', '') + " - no\n")
        
        with open("server/result.txt", "a") as result, open("server/temp.txt", "r") as temp:
          result.write(temp.read())


        if str(data):
          with open("server/temp.txt", 'r') as file:
            message = file.read()
            sock.send(message.encode())
        else:
          sock.close()
          input_socket.remove(sock)

except KeyboardInterrupt:
  server_socket.close()
  sys.exit(0)