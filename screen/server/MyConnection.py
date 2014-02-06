from MyWebsocketServer import WebSocketsHandler
from DevSocketHandler import DevSocketHandler
import SocketServer
import threading

class MyConnection:
    """ wraps all the connection-to-a-websocket stuff """
    def __init__(self, type):
        self.type = type

    def startServer(self):
        print("initializing")
        if (self.type == "web"):
            server = ThreadedServer(("localhost", 9876), WebSocketsHandler)
        else:
            print("listening for devices")
            server = ThreadedServer(("192.168.30.94", 5000), DevSocketHandler)
        server.observer = self
        server.serve_forever()
        #self.server_thread = threading.Thread(target=server.serve_forever)
        #self.server_thread.daemon = True
        #self.server_thread.start()
        #server.serve_forever()

    def send(self, message):
        self.handler.send_message(message)

    def isConnected(self):
        return self.handler is not None

    def kill(self):
# TODO
        pass

    """ handler observer methods """
    def onConnected(self, handler):
        print "MyWebSocket.onConnected"
        self.handler = handler

    def onMessage(self, handler, message):
        print "MyWebSocket.onMessage ", message

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

ws = MyConnection("dev")
ws.startServer()
