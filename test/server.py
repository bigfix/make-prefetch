# This is an HTTP server to respond with 'hodor' to every request. It exists so
# that we can test make-prefetch with different URLs.

import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class HodorHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    hodor = 'hodor'
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', str(len(hodor)))
    self.end_headers()
    self.wfile.write(hodor);
    self.wfile.close();
    return hodor

SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(('127.0.0.1', 36465), HodorHandler)
httpd.serve_forever()
