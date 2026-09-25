from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        html = f"""\
        <html>
        <head><title>Practice server</title></head>
        <body>
            <p>Request: {self.path}</p>
            <p>This is an example web server.</p>
            <p>Response from port: {self.server.server_port}</p>
        </body>
        </html>
        
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))
