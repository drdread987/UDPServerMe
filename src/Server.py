import socketserver


class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("Listening")
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "103.200.110.142", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    print("Started Server")
    server.serve_forever()









