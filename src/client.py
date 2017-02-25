import socket
import sys


HOST, PORT = "103.200.110.142", 9999
data = "Hello! "

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
    sock.close()
except:
    pass


print("Sent:     {}".format(data))
print("Received: {}".format(received))

while received != "STOP":

    received = " "

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        sock.close()
    except:
        break

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))







