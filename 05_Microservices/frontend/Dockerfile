FROM python:3.11-bookworm
WORKDIR /app
COPY server.py .
CMD ["sh", "-c", "python -u server.py || sleep 3600"]