 from http.server import HTTPserver, BaseHTTPRequestHandler

content = """
<html>
<head>
</head>
<body>
    <h1>Welcome</h1>
</body>
</html>
"""

class HelloHandler(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header('content-type','text/html; charset=utf-8')
       self.end_headers()
       self.wfile.write(content.encode())



server_address = ('', 80)
httpd = HTTPserver(server_address, HelloHandler)
httpd.server_forever()