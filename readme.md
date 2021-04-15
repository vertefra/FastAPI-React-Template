# Fastapi React-Typescript template 0.0.1

## Stack

- Python 3.8
- Node 15.0
- Fastapi 0.63
- SQLAlchemy 1.4.4
- Typescript 4.2.3
- React 17.0.2
- Docker/Docker-compose

## Usage

Make sure to create two `.env` files replacing `env-example` in `backend/` folder and in the root project. Database Variables must be the same.

## Backend

Inside `backend/` create a python virtual environment `python3 -m venv .venv`,
activate it (`source .venv/bin/activate`) and install the requirements (`pip3 install -r requirements.txt`)

## Frontend

Inside `frontend/` install all the node modules `npm i`

## Run docker-compose

From the root folder `docker-compose un` to spin the project locally.
Now you can interact with the different services:

- backend `http://localhost:3000`
- frontend `http://localhost:9000`
- db `http://localhost:5432`

You have a basic authentication system with a signup and a login window at

`http://localhost:9000/signup`
`http://localhost:9000/login`