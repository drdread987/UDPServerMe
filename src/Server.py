import threading
import socketserver
import datetime
import time

HOST, PORT = "103.200.110.142", 9999


clients = []


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        global clients
        # self.request is the TCP socket connected to the client
        print("Listening")
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        clients.append(self.client_address[0])
        print(self.data)
        if str(self.data, "utf-8") == "R":
            self.register_client(self.client_address[0])

        self.request.sendall(bytes("STOP", 'UTF-8'))

    def register_client(self, client_ip):

        global clients
        found = False
        for client in clients:
            if client[0] == client_ip:
                found = True
                break
        if not found:
            print("Adding client")
            clients.append([client_ip, datetime.datetime.now()])
            print("Just added the client at: ")
            print(datetime.datetime.now())


def check_alive():
    global clients
    while True:
        print("Checking Alive")
        counter = 0
        remList = []
        for client in clients:
            print(client[1])
            if datetime.datetime.now() - client[1] > datetime.timedelta(0, 5):
                remList.append(counter)
            counter += 1
        for x in remList:
            print("removing a client")
            del clients[x]
        time.sleep(10)

SS = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

th = threading.Thread(target=SS.serve_forever)
ca = threading.Thread(target=check_alive)
th.start()
ca.start()













