# FROM : Tu dis à Docker "Je ne pars pas de zéro, je veux un système d'exploitation qui a déjà Python d'installé".
# python:3.12 : C'est la version de l'image. Tu utilises Python 3.12.
# -slim (Le détail IMPORTANT) :
# Une image python "classique" pèse ~1 Go (elle contient plein d'outils inutiles).
# Une image "slim" pèse ~150 Mo. Elle contient juste le nécessaire pour faire tourner Python.
# Leçon Mentor : En prod, on utilise toujours slim ou alpine pour réduire la surface d'attaque et accélérer les déploiements.
FROM python:3.12-slim

# WORKDIR : Tu dis à Docker "Je veux travailler dans ce dossier".
# C'est l'équivalent de faire un mkdir (créer un dossier) + cd (entrer dedans) dans ton conteneur.
# Généralement : WORKDIR /app.
# Ça veut dire : "Tout ce que je fais après cette ligne se passera dans le dossier /app du conteneur".
WORKDIR /app

# COPY : Tu dis à Docker "Je veux copier des fichiers de mon ordinateur vers le conteneur".
# Web_App.py : C'est le fichier que tu veux copier (depuis ton ordinateur).
COPY Web_App.py .

# EXPOSE : documentation du port d'écoute dans le conteneur.
EXPOSE 8000

# CMD ["python", "main.py"] 
# C'est l'ordre de mission.
# Quand le conteneur démarre (avec docker run), c'est la commande qu'il exécute.
# Pourquoi entre crochets ["...", "..."] ? C'est le format "exec". C'est plus propre car ça lance le processus directement (PID 1)
#, sans passer par un shell (sh). Ça permet de tuer le conteneur proprement (avec Ctrl+C).
# En gros, ça dit : "Lance l'exécutable python avec l'argument Web_App.py".
CMD ["python", "Web_App.py"]


# pour build l'image il faut : 

# 1   docker build -t 02_web_server .
# (Le -t c'est pour lui donner un nom "tag", et le . à la fin c'est TRES important, ça veut dire 
# "cherche le Dockerfile ICI dans ce dossier")

# 2   docker run --rm -p 8080:8000 02_web_server
# (Le -p c'est pour exposer le port 8000 du conteneur sur le port 8080 de ta machine)

# Resultat attendu :
# Ouvre ton navigateur (Chrome/Firefox) et va sur : http://localhost:8080
# Si tu vois le message s'afficher en gros titre... c'est gagné. Tu sais comment exposer une application conteneurisée au monde extérieur. : CHAMPAGNE.