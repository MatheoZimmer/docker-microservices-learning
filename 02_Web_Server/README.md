# 02 — Web Server (Ports & HTTP)

Objectif : exposer un serveur HTTP Python via un port Docker.

Commandes :

- `docker build -t 02_web_server .`
- `docker run --rm -p 8080:8000 02_web_server`

Test : ouvre `http://localhost:8080`.

