# Jaga Aksara (Flask/Backend)

Jaga Aksara is a real time sign language translator

## Installation

Install all PIP dependencies

```sh
 pip install -r requirements.txt
```

Create environtment file from the `example.env` file

```sh
cp .env.example .env
```

Generate secret key, hash key, or JWT secret key into the `.env` file.

```sh
py commands/generate_secret_key.py --env-file .env
# or
python commands/generate_secret_key.py --env-file .env
```

Migrate up/down Jaga Aksara required tables

```sh
alembic upgrade head # to migrate up
# or
alembic downgrade base # to migrate down
```

## Running

Running the application

```
flask --app app.py run
# or
flask --app app.py run --debug # run in debug mode
```

Running the application unit/feature test

```
# The documentation will be there soon...
```

## Docker

You can also deploy to docker container (Dockerizing/Containerizing)

```sh
docker-compose up -d
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:5000
```

## Routes

The application routes are documented in the `postman_collection.json` file.

```sh
head postman_collection.json # check the routes documentation
```

## License

MIT && Jaga Aksara

**Open Source**
