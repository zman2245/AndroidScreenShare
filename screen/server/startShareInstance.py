import subprocess

def startProcess():
    """
    Starts a process in the background and writes a PID file

    returns integer: pid
    """

    # Start process
    process = subprocess.Popen('python MyWebsocketServer.py &', shell=True)

    return process.pid

print "starting process..."
pid = startProcess()
print pid
