import sys
# Mouchard 1 : Démarrage
print("DEBUG [1/6]: Script lancé. Debut des imports...", flush=True)

try:
    import os
    print("DEBUG [2/6]: Import os OK", flush=True)
    
    # On décompose pour voir où ça casse
    import http
    print("DEBUG [2.5/6]: Paquet 'http' OK", flush=True)
    
    import http.server
    print("DEBUG [3/6]: Import http.server OK", flush=True)
    
    import socketserver
    print("DEBUG [4/6]: Import socketserver OK", flush=True)
    
    # C'est souvent lui le coupable dans les images slim
    import urllib.request
    print("DEBUG [5/6]: Import urllib.request OK", flush=True)

    # Configuration
    PORT = int(os.environ.get('PORT', 8000))
    BACKEND_URL = os.environ.get("URL_DU_BACKEND", "http://localhost:5000")
    print(f"DEBUG [6/6]: Config chargée. Port={PORT}, URL={BACKEND_URL}", flush=True)

    class FrontHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            try:
                with urllib.request.urlopen(BACKEND_URL) as response:
                    data = response.read().decode('utf-8')
                html = f"<html><body><h1>Succes</h1><p>{data}</p></body></html>"
                status = 200
            except Exception as e:
                html = f"<html><body><h1>Erreur</h1><p>{e}</p></body></html>"
                status = 500
            
            self.send_response(status)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

    print(f"✅ SERVEUR PRET sur le port {PORT}", flush=True)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), FrontHandler) as httpd:
        httpd.serve_forever()

except Exception as e:
    # Si ça plante n'importe où, on l'affiche !
    print(f"❌ CRASH REPORT: {e}", flush=True)
    # On force une pause pour être sûr que le log a le temps de sortir
    import time
    time.sleep(1)
    sys.exit(1)