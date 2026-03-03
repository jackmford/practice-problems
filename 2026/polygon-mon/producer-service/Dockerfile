FROM python:3.9-slim

WORKDIR /app
COPY pyproject.toml uv.lock /app/

RUN pip install .

COPY polygon-mon/producer-service/poly-producer.py .

EXPOSE 8001

ENV PYTHONBUFFERED=1
CMD ["python", "-u", "poly-producer.py"]

