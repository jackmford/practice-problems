FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir requests prometheus_client

COPY poly-exporter.py .

EXPOSE 8000

CMD ["python", "poly-exporter.py"]
