# **LibraryManager**

A simple RESTful API for managing books, authors, publisher and reviewing it. Authentication with JWT.
Developed in Django Rest Framework using a Postgres database. All services running with Docker.

- Manage books, publishers and authors.
- Add books to read or wish lists.
- Review books and watch other books reviews and stats.

### Run it with docker:
```bash
docker-compose up
```

### Or run it with: 

Install the dependences
```bash
pip install -r requirements.txt 
```

Apply the migrations
```bash
python manage.py migrate
```

Run the application
```bash
python manage.py runserver
```


