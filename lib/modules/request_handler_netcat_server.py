from socketserver import BaseRequestHandler

class RequestHandlerNetcat(BaseRequestHandler):

    _file_handler = None
    _config = None

    def setup(self) -> None:
        self.request.setblocking(False)

    def handle(self) -> None:
        data = b''
        while True:
            try:
                data += self.request.recv(1024)
            except:
                break
        filename = self.file_handler.put_file(path=self.config.paths.datastorage, data=data)
        web_protocol = 'http://'
        if self.config.server.ssl:
            web_protocol = 'https://'
        self.request.send(f'{web_protocol}{self.config.server.address}/{filename}\n'.encode('utf-8'))
        self.request.close()

    @property
    def file_handler(self):
        return self._file_handler

    @file_handler.setter
    def file_handler(self, value):
        self._file_handler = value

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value