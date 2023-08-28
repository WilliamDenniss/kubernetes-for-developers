from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timedelta
import urllib.request
import os
import random

last_ready_time = datetime.now()

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global last_ready_time

        match self.path:
            case '/':
                now = datetime.now()
                response_string = now.strftime("The time is %-I:%M %p, UTC.")
                self.respond_with(200, response_string)
            case '/healthz':
                if (datetime.now() > last_ready_time + timedelta(minutes=5)):
                    self.respond_with(503, "Not Healthy")
                else:
                    self.respond_with(200, "Healthy")
            case '/readyz':
                dependencies_connected = True 
                # TODO: actually verify any dependencies
                if (dependencies_connected):
                    last_ready_time = datetime.now()
                    self.respond_with(200, "Ready")
                else:
                    self.respond_with(503, "Not Ready")
            case _:
                self.respond_with(404, "Not Found")

    def respond_with(self, status_code: int, content: str) -> None:
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open("logs/log.txt", "a") as myfile:
            myfile.write(content + "\n")
        self.wfile.write(bytes(content, "utf-8")) 

def startServer():
    try:
        server = ThreadingHTTPServer(('', 8080), RequestHandler)
        print("Listening on " + ":".join(map(str, server.server_address)))
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

if __name__== "__main__":
    startServer()
