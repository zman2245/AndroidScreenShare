from WebConnection import MyWebSocket

class Screen:
    """ Top-level representation of an ongoing screen share """
    def __init__(self):
        self.webConn = MyWebSocket()
        self.devConn = ""

    def startServer(self):
        self.webConn.startServer()
