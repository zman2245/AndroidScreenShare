import struct
import SocketServer
from base64 import b64encode
from hashlib import sha1
from mimetools import Message
from StringIO import StringIO

class DevSocketHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            print('handle...')
            self.data = self.request.recv(1024).strip()
            self.server.observer.onMessage(self, self.data)
 
    def send_message(self, message):
        self.request.send(message)
