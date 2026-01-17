import http.server
import json

PORT = 5000


class APIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/health"):
            payload = {"status": "ok"}
        else:
            payload = {"message": "Backend reachable via Docker network"}

        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))


if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), APIHandler)
    print(f"Backend API listening on :{PORT}")
    server.serve_forever()