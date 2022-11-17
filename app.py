
from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model


db = PostgresqlDatabase('movies', user='adamkaufman', password='', host='localhost', port='5432')

class BaseModel(Model):
  class Meta:
    database = db

class Movie(BaseModel):
  title = CharField()
  director = CharField()
  release_year = IntegerField()

db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])

Movie(title='Pulp Fiction', director='Quentin Tarantino', release_year=1994).save()
Movie(title='Ferris Bueller\'s Day Off', director='John Hughes', release_year=1986).save()
Movie(title='The Devil Wears Prada', director='David Frankel', release_year=2006).save()
Movie(title='The Breakfast Club', director='John Hughes',release_year=1985).save()
Movie(title='Home Alone', director='John Hughes', release_year=1990).save()
Movie(title='Interstellar', director='Christopher Nolan', release_year=2014).save()

app = Flask(__name__)

@app.route('/movies/', methods=['GET', 'POST'])
@app.route('/movies/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Movie.get(Movie.id == id)))
    else:
        movie_list = []
        for movie in Movie.select():
            movie_list.append(model_to_dict(movie))
        return jsonify(movie_list)

  if request.method =='PUT':
    body = request.get_json()
    Movie.update(body).where(Movie.id == id).execute()
    return "Movie " + str(id) + " has been updated."

  if request.method == 'POST':
    new_movie = dict_to_model(Movie, request.get_json())
    new_movie.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Movie.delete().where(Movie.id == id).execute()
    return "Movie " + str(id) + " deleted."

@app.route('/')
def index():
  return "Hello, world!!!!"


app.run(port=9000, debug=True)