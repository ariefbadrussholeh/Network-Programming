import socket

print("Masukkan IP Server")
server_ip = input()
print("Masukkan Port Server")
port_ip = input()

server_address = (server_ip, int(port_ip))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

print("Masukkan pesan yang akan dikirim")
strsend = input()

client_socket.send(strsend.encode())

data = client_socket.recv(1024).decode()
print(data)

client_socket.close()