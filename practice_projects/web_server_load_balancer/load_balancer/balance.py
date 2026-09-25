from http.server import BaseHTTPRequestHandler
from urllib.request import urlopen

class Balance():
    def __init__(self, servers: list[str]):
        self.servers = servers
        self.counter = 0

    def next_server(self):
        server = self.servers[self.counter]
        self.counter += 1
        if self.counter == len(self.servers):
            self.counter = 0
        return server

class BalanceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        selected = self.server.balancer.next_server()
        request_url = (f"http://{selected}{self.path}")

        with urlopen(request_url, timeout=3) as backend_response:
            body = backend_response.read()

            self.send_response(backend_response.status)
            self.send_header("Content-Type", backend_response.headers.get("Content-Type", "text/html; charset=utf-8"))
            self.send_header("Content-Lenght", str(len(body)))
            self.end_headers()
            self.wfile.write(body)