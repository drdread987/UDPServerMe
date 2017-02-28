import socket
import datetime

UDP_IP = "103.200.110.142"
UDP_PORT = 9999
MESSAGE = bytes("HELLO, WORLD!", "utf-8")

self_UDP_IP = "25.16.137.215"
self_UDP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = datetime.datetime.now()


counter = 0
while 1:

    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    sock.bind((self_UDP_IP, self_UDP_PORT))
    data, addr = sock.recvfrom(1024)
    if data == "STOP":
        break
    else:
        print(data)
s.close()






