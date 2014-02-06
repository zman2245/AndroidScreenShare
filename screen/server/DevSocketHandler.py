import SocketServer
from base64 import b64encode
from StringIO import StringIO

class DevSocketHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.server.observer.onConnected(self)
        while True:
            self.data = self.request.recv(64000).strip()
            self.server.observer.onMessage(self, "device", self.data)
 
    def send_message(self, message):
        self.request.send(message)
