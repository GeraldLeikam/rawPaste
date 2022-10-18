from http.server import BaseHTTPRequestHandler
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import guess_lexer


class RequestHandlerWeb(BaseHTTPRequestHandler):

    charset = 'utf-8'

    _file_handler = None
    _config = None

    server_version = 'xws'
    sys_version = ''

    def _set_response(self, response_code):
        self._send_response(response_code)
        self._send_header()

    def _send_header(self):
        self.send_header('Content-type', f'text/html; charset={self.charset.upper()}')
        self.end_headers()

    def _send_response(self, response_code):
        message = ''
        if response_code == 200:
            message = 'OK'

        self.send_response(response_code, message)

    def do_HEAD(self):
        self._set_response(response_code=200)

    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self.get_index()
        if self.path == '/favicon.png':
            self.get_favicon(url_path=self.path)
        if '.css' in self.path:
            self.get_stylesheet(self.path)
        self.connection.close()
    """
    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self._set_response(response_code=200)
            self.get_index(self.path)
        if self.path == '/favicon.png':
            self._set_response(response_code=200)
            self.get_favicon(self.path)
        else:
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
    """

    def get_index(self):
        index = self.file_handler.get_file(path=self.config.paths.htmlstorage, filename='index.html')
        if index != None:
            self.send_response(200, 'OK')
            self.send_header('Content-type', f'text/html; charset={self.charset.upper()}')
            self.end_headers()
            self.wfile.write(index)
        else:
            self.send_response(404, 'Not Found')
            self.send_header('Content-type', f'text/html; charset={self.charset.upper()}')
            self.end_headers()

    def get_favicon(self, url_path):
        favicon = self.file_handler.get_file(path=self.config.paths.faviconstorage, filename=url_path[1:])
        if favicon != None:
            self.send_response(200, 'OK')
            self.send_header('Content-type', f'image/x-icon')
            self.end_headers()
            self.wfile.write(favicon)
        else:
            self.send_response(404, 'Not Found')
            self.send_header('Content-type', f'image/x-icon')
            self.end_headers()

    def get_stylesheet(self, url_path):
        stylesheet = self.file_handler.get_file(path=self.config.paths.stylesheetstorage, filename=url_path[1:])
        if stylesheet != None:
            self.send_response(200, 'OK')
            self.send_header('Content-type', f'text/css')
            self.end_headers()
            self.wfile.write(stylesheet)
        else:
            self.send_response(404, 'Not Found')
            self.send_header('Content-type', f'text/css')
            self.end_headers()

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