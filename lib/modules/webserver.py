from lib.modules.threaded_server import ThreadedServer
from lib.modules.request_handler_webserver import RequestHandlerWeb
from sys import stdout

class Webserver():

    def __init__(self, config, file_handler):
        requestHandler = RequestHandlerWeb
        requestHandler.config = config
        requestHandler.file_handler = file_handler
        webserver = ThreadedServer(
            (
                str(config.server.address),
                int(config.server.webport)
            ),
            RequestHandlerWeb
        )
        while True:
            stdout.flush()
            webserver.handle_request()