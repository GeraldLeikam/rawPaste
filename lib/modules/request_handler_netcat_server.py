from socketserver import BaseRequestHandler
from lib.modules import file_system

class RequestHandlerNetcat(BaseRequestHandler):

    _file_handler = None
    _config = None

    _web_protocol = 'http'

    def setup(self) -> None:
        self.request.setblocking(False)

    def handle(self) -> None:
        print(f'getting request from {self.client_address}')
        data = b''
        while True:
            try:
                data += self.request.recv(1048576)
                try:
                    print(round(len(data)/1048576, 2))
                except:
                    print(0)
            except:
                break
        filename = file_system.generate_filename()
        #print(filename)
        file_system.write_file(path=self.config.paths.datastorage, filename=filename, content=data)
        if self.config.server.ssl:
            self._web_protocol = 'https'
        self.request.send(f'{self._web_protocol}://{self.config.server.address}/{filename}\n'.encode('utf-8'))
        self.request.close()

    @property
    def file_handler(self):
        return self._file_handler

    @file_handler.setter
    def file_handler(self, value):
        self._file_handler = value

    @property
    def config(self): return self._config

    @config.setter
    def config(self, value): self._config = value