# python-and-flask

Movie API using Python, Flask, and Postgres

Running on port 9000

Root directory: localhost:9000/

# Model

```
class Movie(BaseModel):
  title = CharField()
  director = CharField()
  release_year = IntegerField()
```

# Routes

localhost:9000/movies

localhost:9000/movies/id

# CRUD

## GET request
Get all movies using the link:
localhost:9000/movies

Get individual movie by id using the link: localhost:9000/movies/id

localhost:9000/movies/1 will return:

```
{
  "director": "Quentin Tarantino",
  "id": 1,
  "release_year": 1994,
  "title": "Pulp Fiction"
}
```

## CREATE
Post a new movie to the localhost:9000/movies route following the class model

## UPDATE and DELETE
Put and delete by id using the route localhost:9000/movies/id