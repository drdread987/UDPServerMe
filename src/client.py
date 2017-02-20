import socket

HOST = "103.200.110.142"
PORT = 9999
readbuffer = ""

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("Hello server", "UTF-8"))


while True:
    readbuffer = str(s.recv(1024))

    temp = readbuffer.split("\n")

    for line in temp:
        print(line)





