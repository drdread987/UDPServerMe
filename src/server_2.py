import socket


UDP_IP = "103.200.110.142"
UDP_PORT = 9999
BUFFER_SIZE = 1024

MESSAGE = bytes("STOP", "utf-8")

target_ip = "25.16.137.215"
target_port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))


while 1:
    data, addr = s.recvfrom(1024)
    # target_ip = addr[0]
    if not data:
        break
    else:
        print("sending data to : " + target_ip)
        sock.sendto(MESSAGE, (target_ip, target_port))
    print(data)


