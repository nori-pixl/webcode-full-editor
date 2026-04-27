import http.server
import socketserver
import os

# Renderから指定されるポートを取得、デフォルトを10000に設定
PORT = int(os.environ.get("PORT", 10000))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    # index.htmlをデフォルトで開く設定
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
