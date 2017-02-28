import socket
import datetime

UDP_IP = "103.200.110.142"
UDP_PORT = 9999
MESSAGE = bytes("HELLO, WORLD!", "utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = datetime.datetime.now()

counter = 0
while 1:
    ping_start = datetime.datetime.now()
    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    break
s.close()






