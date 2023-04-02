FROM python:3.8-slim-buster

ARG FASTAPI_PORT=8000
ARG OMP_NUM_THREADS=1

ENV PORT=$FASTAPI_PORT
ENV OMP_NUM_THREADS=$OMP_NUM_THREADS

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && apt-get update && \
    apt-get install -y libgomp1 && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/

EXPOSE $FASTAPI_PORT

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "${PORT}"]
