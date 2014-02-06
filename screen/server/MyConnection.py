from WebSocketHandler import WebSocketHandler
from DevSocketHandler import DevSocketHandler
import SocketServer
import threading

class MyConnection:
    """ wraps all the connection-to-a-websocket stuff """

    """ observer must implement onConnected, onMessage"""
    def __init__(self, observer, src):
        self.src = src
        self.observer = observer

    def startServer(self):
        print("initializing: ",self.src)
        if (self.src == "web"):
            server = ThreadedServer(("localhost", 9876), WebSocketHandler)
        else:
            print("listening for devices")
            server = ThreadedServer(("192.168.30.94", 5000), DevSocketHandler)
        server.observer = self
        self.server_thread = threading.Thread(target=server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        #server.serve_forever()

    def send(self, message):
        if hasattr(self, 'handler'):
            self.handler.send_message(message)

    def isConnected(self):
        return self.handler is not None

    def kill(self):
# TODO
        pass
    
    """ handler observer methods """
    def onConnected(self, handler):
        print ("onConnection:")
        self.handler = handler
        self.observer.onConnected(handler)

    def onMessage(self, handler, src, message):
        print ("onMessage ",message)
        self.observer.onMessage(handler, src, message)

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True
