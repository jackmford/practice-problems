FROM python:3.9-slim

WORKDIR /app
COPY pyproject.toml uv.lock /app/

RUN pip install .

COPY polygon-mon/exporter-service/poly-exporter.py .

EXPOSE 8000

CMD ["python", "poly-exporter.py"]
