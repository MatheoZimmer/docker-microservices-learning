FROM python:3.12-slim
WORKDIR /app
COPY server.py .
CMD ["sh", "-c", "python -u server.py || sleep 3600"]