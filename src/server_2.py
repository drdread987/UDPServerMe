import socket


TCP_IP = "103.200.110.142"
TCP_PORT = 9999
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print("Connection Address: ", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("Received data: ", data)
    conn.send(bytes("I SEE YOU ARE ALSO A BOT", "utf-8"))
conn.close()

