# frontend/server.py
import http.server
import socketserver
import urllib.request
import os  # <--- On a besoin de l'OS pour lire les variables

PORT = 8000

# ON NE MET PLUS L'URL EN DUR !
# On dit : "Cherche la variable 'URL_DU_BACKEND', sinon prends une valeur par défaut"
BACKEND_URL = os.environ.get("URL_DU_BACKEND", "http://localhost:5000")

class FrontHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # On affiche quelle URL on appelle (pour le debug)
            print(f"Tentative de connexion vers : {BACKEND_URL}")
            
            with urllib.request.urlopen(BACKEND_URL) as response:
                data = response.read().decode('utf-8')
            
            html_content = f"""
            <html>
                <body>
                    <h1>Interface Frontend Pro</h1>
                    <p>Configuration chargée via Docker Env : <b>{BACKEND_URL}</b></p>
                    <p>Réponse du Backend :</p>
                    <h2 style='color:green'>{data}</h2>
                </body>
            </html>
            """
            status = 200
        except Exception as e:
            html_content = f"<h1>Erreur</h1><p>Impossible de joindre {BACKEND_URL}</p><p>{e}</p>"
            status = 500

        self.send_response(status)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

with socketserver.TCPServer(("0.0.0.0", PORT), FrontHandler) as httpd:
    print(f"Frontend demarré. Cible backend : {BACKEND_URL}")
    httpd.serve_forever()