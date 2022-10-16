from socketserver import TCPServer
from socketserver import ThreadingMixIn

class ThreadedServer(ThreadingMixIn, TCPServer):
    pass