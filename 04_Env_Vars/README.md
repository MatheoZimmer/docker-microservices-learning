# 04 — Env Vars (Configuration Externalisée)

Objectif : injecter la configuration via variables d'environnement (ex : ports, noms de conteneurs).

Installation :

```bash
cp .env.example .env
docker compose up --build
```

Test : ouvre `http://localhost:8080`.