FROM python:3.11-bookworm

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY api.py .
EXPOSE 5000

CMD ["python", "api.py"]