import socket
import datetime

UDP_IP = "103.200.110.142"
UDP_PORT = 9999
MESSAGE = bytes("HELLO, WORLD!", "utf-8")

self_UDP_IP = "localhost"
self_UDP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = datetime.datetime.now()
s.bind((self_UDP_IP, self_UDP_PORT))

counter = 0
while 1:
    data, addr = s.recvfrom(1024)
    ping_start = datetime.datetime.now()
    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    if data == "STOP":
        break
    else:
        print(data)
s.close()






