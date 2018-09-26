import socket

s  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 3333

address = (host, port)

s.bind(address)
print('server started')

while True:
    data, addr = s.recvfrom(1024)
    print('data from {}'.format(addr))
    datarecv = data.decode('utf-8')
    if datarecv == 'exit':
        print('exiting out of program')
        emsg = 'Received Message thank you'
        emsg = emsg.encode('utf-8')
        s.sendto(emsg, addr)
        break
    else:
        print('data received:', datarecv)
        msg = 'Received Message thank you'
        sendmsg = msg.encode('utf-8')
        s.sendto(sendmsg, addr)


