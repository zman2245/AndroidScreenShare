from MyConnection import MyConnection

class Screen:
    """ Top-level representation of an ongoing screen share """
    def __init__(self):
        self.webConn = MyConnection(self, "web")
        self.devConn = MyConnection(self, "device")

    def startServer(self):
        self.webConn.startServer()
        self.devConn.startServer()
        print("all servers started")

    """ handler observer methods """
    def onConnected(self, handler):
        print ("onConnection:")

    def onMessage(self, handler, src, message):
        print ("onMessage ",message)
        if (src == "device"):
            self.webConn.send(message)

s = Screen()
s.startServer()

while True:
    pass
