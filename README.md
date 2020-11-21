# Diet generator

This is a project for Project Management and Evaluation class (TI2011) at Tec de Monterrey.

## Setup
It's important that you've installed Docker, since it's mandatory to run the environment.

Clone the repo, `cd` into the project and run:

```bash
docker-compose up
```
This will build the image and start the server.

Check your `http://localhost:8000/` and if you see something, you're good to go.

At your console you would a message indicating that you have pending migrations. You can see which ones with:
```bash
docker-compose run api python manage.py showmigrations
```

Run them:
```bash
docker-compose run api python manage.py migrate
```

To start with some data you can run a script:
```bash
docker-compose run api python manage.py runscript load_initial_data
```
It's important that your database is as fresh as new.
If you have data and don't mind to loose it, do the following **before** loading the data:
```bash
docker-compose run api python manage.py reset_db
docker-compose run api python manage.py migrate
```

## Shutting down the dev server
Press `CTRL+C` at the running terminal and wait for the containers to stop, the enter `docker-compose down`.

## Note
Ask the owner for the secret key.
