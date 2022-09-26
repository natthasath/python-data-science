from gevent import sleep, socket
from gevent.server import StreamServer

class Connection:
    def __init__(self, host, port):
        self.server = StreamServer((host, port), self.handle)
        self.data = []
        self.socks = []
        self.pointer = 0

    def handle(self, sock, address):
        self.socks.append(sock)
        while True:
            line = sock.recv(1024)
            if line:
                self.data += [line]
            else:
                break
        sock.close()
        self.socks.remove(sock)

    def send(self, msg):
        if self.socks:
            sock2send = self.socks[-1]
            try:
                sock2send.send(msg)
            except(IOError, e):
                print("Can't send message '%s'! Exception:") % msg, e
        else:
            print("No sockets to send the message to")

    def start(self):
        self.server.start()

    def serve_forever(self):
        self.server.serve_forever()

    def close(self):
        self.server.stop()
        for sock in self.socks:
            sock.close()

    def new_data(self):
        newest = self.data[self.pointer:]
        self.pointer = len(self.data)
        return newest

    def testTCPClient(self):    
        j = lambda x: "".join(x)

        server = Connection("", 5555)            
        server.start()
        client.run()
        sleep(3)
        data = j(server.new_data())
        self.assertTrue("login" in data)
        sleep(2)
        server.send("login approve")
        sleep(2)
        data = j(server.new_data())
        self.assertTrue("after_login" in data)
        server.send("logout")
        sleep(2)
        data = j(server.new_data())
        self.assertTrue("received_logout" in data)
        server.close()
        self.assertTrue("disconnected" in client.logs)
