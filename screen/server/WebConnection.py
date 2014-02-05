from MyWebsocketServer import WebSocketsHandler
import SocketServer

class MyWebSocket:
    """ wraps all the connection-to-a-websocket stuff """
    
    def startServer(self):
        print("initializing")
        server = ThreadedServer(("localhost", 9876), WebSocketsHandler)
        server.observer = self
        server.serve_forever()

    """ handler observer methods """
    def onConnected(self, handler):
        print "MyWebSocket.onConnected"

    def onMessage(self, handler, message):
        print "MyWebSocket.onMessage ", message

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

ws = MyWebSocket()
ws.onConnected("hi")
ws.startServer()

