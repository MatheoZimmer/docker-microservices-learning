import http.server
import os
import urllib.request

PORT = int(os.environ.get("PORT", "8000"))
BACKEND_URL = os.environ.get("URL_DU_BACKEND", "http://localhost:5000")


class FrontHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/health"):
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"ok")
            return

        try:
            with urllib.request.urlopen(BACKEND_URL, timeout=2) as response:
                backend_payload = response.read().decode("utf-8")

            body = f"""
            <html>
              <body>
                <h1>Frontend</h1>
                <p>Backend URL: <b>{BACKEND_URL}</b></p>
                <pre>{backend_payload}</pre>
              </body>
            </html>
            """
            status = 200
        except Exception as e:
            body = f"""
            <html>
              <body>
                <h1>Backend unreachable</h1>
                <p>{BACKEND_URL}</p>
                <pre>{e}</pre>
              </body>
            </html>
            """
            status = 502

        self.send_response(status)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), FrontHandler)
    print(f"Frontend listening on :{PORT} (backend={BACKEND_URL})")
    server.serve_forever()