import socket

#AF_INET = ipv4 protocol
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4000

address = (host, port)

serversocket.bind(address)
serversocket.listen(1)

while True:
    clientsocket, address = serversocket.accept()
    print('received connection from {}'.format(str(address)))
    message = 'You are now connected to the server'
    message = message.encode('utf-8')
    clientsocket.send(message)

    clientsocket.close()
print('closed')

