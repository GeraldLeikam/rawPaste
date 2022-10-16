from lib.modules.threaded_http_server import ThreadedHTTPServer
from lib.modules.request_handler_webserver import RequestHandlerWeb
from sys import stdout

class Webserver():

    def __init__(self, config, file_handler):
        requestHandler = RequestHandlerWeb
        requestHandler.config = config
        requestHandler.file_handler = file_handler
        webserver = ThreadedHTTPServer(
            (
                str(config.server.address),
                int(config.server.webport)
            ),
            RequestHandlerWeb
        )
        while True:
            stdout.flush()
            webserver.handle_request()