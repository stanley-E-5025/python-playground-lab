import http.server
import socketserver
import urllib.request


class ProxyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Check if the request is secure (https)
        if self.headers.get("Upgrade") != "HTTPS":
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Error: Request not secure</h1>")
            return
        
        # Add client information to the header
        headers = urllib.request.urlopen(self.path).info()
        headers.add_header("X-Forwarded-For", self.client_address[0])
        headers.add_header("X-Forwarded-By", "My-Proxy-Server")
        
        # Forward the request to the target server
        req = urllib.request.urlopen(urllib.request.Request(self.path, headers=headers))
        
        # Send the response back to the clients
        self.send_response(req.getcode())
        self.send_header("Content-type", req.info()["Content-type"])
        self.end_headers()
        self.wfile.write(req.read())

# Create the server and set it to listen on localhost:5000
httpd = socketserver.TCPServer(("localhost", 5000), ProxyHandler)
httpd.serve_forever()
