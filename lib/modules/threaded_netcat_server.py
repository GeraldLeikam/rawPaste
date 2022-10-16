from socketserver import TCPServer
from socketserver import ThreadingMixIn

class ThreadedNetcatServer(ThreadingMixIn, TCPServer):
    pass