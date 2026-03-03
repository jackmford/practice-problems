FROM python:3.9-slim

WORKDIR /app
COPY pyproject.toml uv.lock /app/

RUN pip install .

COPY polygon-mon/relay-service/poly-relay.py .

EXPOSE 8001

ENV PYTHONBUFFERED=1
CMD ["python", "-u", "poly-relay.py"]
