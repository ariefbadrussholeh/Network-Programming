import select
import socket
import sys
import threading
import re

client_sockets = []

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def run(self):
        self.open_socket()
        input = [self.server]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])

            for s in inputready:
                if s == self.server:
                    # handle the server socket
                    client_socket, client_address = self.server.accept()
                    client_sockets.append(client_socket)
                    c = Client(client_socket, client_address)
                    c.start()
                    self.threads.append(c)
                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0

	 # close all threads
        self.server.close()
        for c in self.threads:
            c.join()

class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            data = str(data.decode())
            data = data.split("~")

            print("Menerima file \"{}\" dari {} - mengirimkan ke semua client terhubung".format(data[0], str(self.address)))
            
            message = "{}~{}".format(data[0], data[1])
            if data:
                for client_socket in client_sockets:
                    if client_socket != self.client:
                        client_socket.send(message.encode())

                self.client.send("File berhasil terkirim\n".encode())
            else:
                self.client.close()
                running = 0

if __name__ == "__main__":
    s = Server()
    s.run()