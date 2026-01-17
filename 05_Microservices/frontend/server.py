print("DEBUG: Initialisation du script Python...", flush=True)

import http.server
import socketserver
import urllib.request
import os
import sys

# On sécurise le démarrage
try:
    print("DEBUG: Lecture des variables d'environnement...", flush=True)
    # Conversion explicite en INT pour éviter le crash TypeError
    PORT = int(os.environ.get('PORT', 8000))
    BACKEND_URL = os.environ.get("URL_DU_BACKEND", "http://localhost:5000")
    
    print(f"DEBUG: Config chargée. Port={PORT}, Backend={BACKEND_URL}", flush=True)

    class FrontHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            try:
                print(f"Tentative de connexion vers : {BACKEND_URL}", flush=True)
                with urllib.request.urlopen(BACKEND_URL) as response:
                    data = response.read().decode('utf-8')
                html_content = f"<html><body><h1>Succes!</h1><p>{data}</p></body></html>"
                status = 200
            except Exception as e:
                html_content = f"<h1>Erreur</h1><p>{e}</p>"
                status = 500
            
            self.send_response(status)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))

    print(f"Frontend demarré sur le port {PORT}. En attente...", flush=True)
    
    # Lancement du serveur
    with socketserver.TCPServer(("0.0.0.0", PORT), FrontHandler) as httpd:
        httpd.serve_forever()

except Exception as e:
    # Si ça plante, on l'écrit
    print(f"CRITICAL ERROR: {e}", file=sys.stderr, flush=True)
    sys.exit(1)