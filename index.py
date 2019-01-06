#!/usr/bin/python
'''
    Simple webserver in python that implements a hello python message
    for the microservices kubernetes tutorial
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Basic request handler for the webserver
class RequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):
        switcher = {
            "/": self.index,
            "/health": self.health,
        }
        func = switcher.get(self.path, self.notfound)
        func()
        return

    def index(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write('Hello Python!')
        return

    def health(self):
        self.send_response(204)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        return

    def notfound(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write('Resource not found')
        return

try:
    server = HTTPServer(('',8000), RequestHandler)
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()