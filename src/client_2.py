import socket

TCP_IP = "103.200.110.142"
TCP_PORT = 9999
BUFFER_SIZE = 1024
MESSAGE = "HELLO, WORLD!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data: " + data)




