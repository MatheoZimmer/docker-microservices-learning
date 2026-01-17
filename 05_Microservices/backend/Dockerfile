FROM python:3.11-slim
WORKDIR /app
COPY api.py .
CMD ["sh", "-c", "python -u api.py || sleep 3600"]