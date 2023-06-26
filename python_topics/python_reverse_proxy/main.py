import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests


class ReverseProxy(BaseHTTPRequestHandler):

    def do_GET(self):
        target_response = requests.get(target_url + self.path)
        self.send_response(target_response.status_code)
        self.send_header('Content-type', target_response.headers['Content-Type'])
        self.end_headers()
        self.wfile.write(target_response.content)

    def do_POST(self):
        content_length = int(self.headers.getheader('content-length'))
        post_data = self.rfile.read(content_length)
        target_response = requests.post(target_url + self.path, data=post_data)
        self.send_response(target_response.status_code)
        self.send_header('Content-type', target_response.headers['Content-Type'])
        self.end_headers()
        self.wfile.write(target_response.content)

target_url = "https://conectar.ch" # replace this with the target website's url
server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, ReverseProxy)
print('Starting reverse proxy on localhost:8080')
httpd.serve_forever()
