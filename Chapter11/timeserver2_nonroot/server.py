from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        now = datetime.now()
        response_string = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("logs/log.txt", "a") as myfile:
            myfile.write(response_string + "\n")
        self.wfile.write(bytes(response_string,"utf-8"))

def startServer():
    try:
        server = ThreadingHTTPServer(('',8080), RequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

if __name__== "__main__":
    startServer()
