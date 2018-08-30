from http.server import SimpleHTTPRequestHandler
import socketserver
import logging
import os
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPRequestHandler.do_GET(self)

os.chdir(Path('.') / 'flask')

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    httpd.serve_forever()
