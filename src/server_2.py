import socket


UDP_IP = "103.200.110.142"
UDP_PORT = 9999
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))


while 1:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    print(data)


