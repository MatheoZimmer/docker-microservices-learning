import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", "8000"))

# Ce Handler sert juste à dire "Coucou" quand on l'appelle
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Bravo Matheo ! Tu es un DevOps maintenant.</h1>")

# On lance le serveur qui écoute PARTOUT (0.0.0.0 est vital dans Docker)
with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"Serveur en cours d'execution sur le port {PORT}")
    httpd.serve_forever()