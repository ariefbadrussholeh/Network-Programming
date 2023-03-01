import socket

print("Masukkan IP Server")
server_ip = input()
print("Masukkan Port Server")
port_ip = input()

server_address = (server_ip, int(port_ip))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

print("Masukkan file yang akan dikirim")
file_name = input()

file_data = open("client/" + file_name, "r").read()
# print(file_data)

strsend = file_name + " " + file_data
client_socket.send(strsend.encode())
client_socket.close()