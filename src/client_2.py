import socket
import datetime

TCP_IP = "103.200.110.142"
TCP_PORT = 9999
BUFFER_SIZE = 1024
MESSAGE = bytes("HELLO, WORLD!", "utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
start_time = datetime.datetime.now()
counter = 0
while 1:
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    current_time = datetime.datetime.now()
    counter += 1
    if current_time - start_time > datetime.timedelta(0, 60):
        break
s.close()
print(counter)






