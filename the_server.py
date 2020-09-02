from http.server import HTTPServer, BaseHTTPRequestHandler

class the_server(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try:
			fto = open(self.path[1:]).read()
			self.send_response(200)
		except:
			fto = '404 File not found'
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(fto, 'utf-8'))

hhttpp = HTTPServer(('localhost', 8080), the_server)
hhttpp.serve_forever()
