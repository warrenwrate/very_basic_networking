import socket

#AF_INET = ipv4 protocol
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# should be same as 127.0.0.1 when testing
host = socket.gethostname()
port = 4000

address = (host, port)

clientsocket.connect(address)
message = clientsocket.recv(1024)
print(message)
clientsocket.close()

