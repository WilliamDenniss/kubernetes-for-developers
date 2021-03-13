# docs: https://docs.python.org/3/library/http.server.html

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes("Hello docker","utf-8")) 

def startServer():
    try:
        server = ThreadingHTTPServer(('',80), RequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

if __name__== "__main__":
    startServer()
