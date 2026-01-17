# backend/api.py
import http.server
import socketserver
import json

PORT = 5000

class APIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # On prépare la réponse JSON
        reponse = {"message": "Bravo ! Tu as hacké le Backend via Docker Network !"}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(reponse).encode('utf-8'))

# Lancement du serveur
with socketserver.TCPServer(("0.0.0.0", PORT), APIHandler) as httpd:
    print(f"Backend (API) en écoute sur le port {PORT}")
    httpd.serve_forever()