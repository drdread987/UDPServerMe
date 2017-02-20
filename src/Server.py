import socketserver
counter = 0


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        print("Listening")
        global counter
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        counter += 1
        if counter < 10:
            self.request.sendall(bytes("I heard you, you stupid client", 'UTF-8'))
        else:
            self.request.sendall(bytes("STOP", 'UTF-8'))

if __name__ == "__main__":
    HOST, PORT = "103.200.110.142", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()









