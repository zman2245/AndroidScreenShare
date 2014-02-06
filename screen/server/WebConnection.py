from MyWebsocketServer import WebSocketsHandler
import SocketServer
import threading

class MyWebSocket:
    """ wraps all the connection-to-a-websocket stuff """
    
    def startServer(self):
        print("initializing")
        server = ThreadedServer(("localhost", 9876), WebSocketsHandler)
        server.observer = self
        self.server_thread = threading.Thread(target=server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
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

#ws = MyWebSocket()
#print("starting thread")
#ws.startServer()

print "hello"
