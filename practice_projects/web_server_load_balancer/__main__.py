import argparse
from http.server import HTTPServer

from .servers.server import MyServer
from .load_balancer.balance import Balance, BalanceHandler

hostName = "localHost"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int)
    parser.add_argument("--role", choices=["backend", "balancer"], default="backend", help="Milyen típusú webservert indítson.")

    args = parser.parse_args()

    if args.port:
        if args.role == "balancer":
            webServer = HTTPServer((hostName, args.port), BalanceHandler)
            balancer = Balance([
                    "localhost:8001",
                    "localhost:8002",
                    "localhost:8003",
                ])
            webServer.balancer = balancer
        else:
            webServer = HTTPServer((hostName, args.port), MyServer)
        
        print(f"Server started http://%s:%s" % (hostName, args.port))

        try:
            webServer.serve_forever()

        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")