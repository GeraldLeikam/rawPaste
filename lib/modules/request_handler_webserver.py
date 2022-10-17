from http.server import BaseHTTPRequestHandler
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import guess_lexer


class RequestHandlerWeb(BaseHTTPRequestHandler):

    charset = 'utf-8'

    _file_handler = None
    _config = None


    def _set_response(self, response_code):
        self.send_response(response_code)
        self.send_header('Content-type', f'text/html; charset={self.charset}')
        self.end_headers()

    def do_HEAD(self):

        self.send_response(200, 'OK')
        self.send_header('Content-type', f'text/html; charset={self.charset}')
        self.send_header('Server', 'xws')
        self.end_headers()

    def do_GET(self):
        print(dir(self.server))
        file_data = self.file_handler.get_file(filename=self.path[1:])
        if file_data is not None:
            self._set_response(200)
            if 'curl' in self.headers['User-Agent'].lower() or 'wget' in self.headers['User-Agent'].lower():
                self.wfile.write(file_data)
            else:
                lexer = guess_lexer(file_data)
                formatter = HtmlFormatter(linenos=False, full=False)
                answer = highlight(file_data, lexer, formatter)
                self.wfile.write(answer.encode('utf-8'))
        else:
            self._set_response(404)
            self.wfile.write('File not found'.encode('utf-8'))

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