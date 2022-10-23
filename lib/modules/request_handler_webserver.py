from http.server import BaseHTTPRequestHandler
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import guess_lexer
from lib.modules import file_system

class RequestHandlerWeb(BaseHTTPRequestHandler):

    charset = 'utf-8'

    _file_handler = None
    _config = None

    server_version = 'xws'
    sys_version = ''

    response_codes_messages = {
        200: 'OK',
        404: 'Not Found',
    }

    content_types = {
        'html': f'text/html; charset={charset}',
        'plain': f'text/plain; charset={charset}',
        'css': f'text/css; charset={charset}',
        'jpg': f'image/jpg;',
        'png': f'image/png;',
        'none': None,
    }

    def _send_response(self, response_code, content_type):
        self.send_response(response_code, self.response_codes_messages[response_code])
        self.send_header('Content-type', self.content_types[content_type])
        self.end_headers()

    def do_HEAD(self):
        self._send_response(response_code=200, content_type='plain')

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        content = file_system.read_file(path=self.config.paths.htmlstorage, filename=self.path[1:])
        content_type = self.path[1:].split('.')[len(self.path[1:].split('.')) - 1]
        if content == b'':
            content = file_system.read_file(path=self.config.paths.datastorage, filename=self.path[1:])
            content_type = 'plain'
        if content != b'':
            self._send_response(response_code=200, content_type=content_type)
            self.wfile.write(content)
        else:
            self.path = '/404.html'
            content = file_system.read_file(path=self.config.paths.htmlstorage, filename=self.path[1:])
            content_type = self.path[1:].split('.')[len(self.path[1:].split('.')) - 1]
            self._send_response(response_code=404, content_type=content_type)
            self.wfile.write(content)

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value