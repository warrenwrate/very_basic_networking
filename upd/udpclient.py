import socket

s  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 3334

address = (host, port)

server = (host, 3333)

s.bind(address)
print('server started')

while True:
    message = input("enter message:")
    s.sendto(message.encode('utf-8'), server)
    data, addr = s.recvfrom(1024)
    print('data received:', data.decode('utf-8'))
    if message == 'exit':
        print('terminating client')
        break