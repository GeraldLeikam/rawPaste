from lib.modules.threaded_netcat_server import ThreadedNetcatServer
from lib.modules.request_handler_netcat_server import RequestHandlerNetcat
from sys import stdout

class NetcatServer:
    def __init__(self, config, file_handler):
        requestHandler = RequestHandlerNetcat
        requestHandler.file_handler = file_handler
        requestHandler.config = config
        netcat_server = ThreadedNetcatServer(
            (
                config.server.address,
                config.server.netcatport
            ),
            requestHandler
        )
        while True:
            stdout.flush()
            netcat_server.handle_request()

