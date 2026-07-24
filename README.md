# pythondocker

This repository contains a simple FastAPI app configured to run in Docker.

## Endpoints

- `GET /` - root greeting
- `GET /health` - health check
- `GET /items/{item_id}` - get item details
- `POST /items` - create a new item

## Run with Docker

Build the image:

```bash
docker build -t fastapi-demo .
```

Run the container:

```bash
docker run --rm -p 8000:8000 fastapi-demo
```

Open `http://localhost:8000` in your browser.
