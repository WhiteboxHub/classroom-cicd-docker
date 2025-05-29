# classroom-cicd-docker

## Clone the Repository

```bash
git clone https://github.com/WhiteboxHub/classroom-cicd-docker.git
cd classroom-cicd-docker
git checkout dev
```

## Build and Run the Simple API with Docker

Navigate to the `classroom-cicd-docker` directory:

```bash
cd classroom-cicd-docker
```

Build the Docker image:

```bash
docker build -t simple-api .
```

Run the container:

```bash
docker run -p 8000:8000 simple-api
```

### API Endpoints

- `GET /` — Welcome message
- `GET /hello/{name}` — Greet a user by name
- `POST /items/` — Create an item with name and price

---

## Working with Docker Compose (Multiple Services)

Navigate to the `docker-compose-example` folder:

```bash
cd docker-compose-example
```

You will see two services: `service1` and `service2`.

To run both services:

```bash
docker-compose up
```

### Service Endpoints

- Service 1: `GET /service1` at [http://localhost:8001/service1](http://localhost:8001/service1)
- Service 2: `GET /service2` at [http://localhost:8002/service2](http://localhost:8002/service2)

---

## Collaborators

- whitebox-learning

