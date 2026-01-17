FROM python:3.11-bookworm

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY server.py .
EXPOSE 8000

CMD ["python", "server.py"]