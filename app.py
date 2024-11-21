from flask import Flask
from utils import *


app = Flask(__name__, template_folder='templates')

@app.route('/movie/<title>')
def get_movie(title):
    film = get_movie_by_title(title)
    return film

@app.route('/movie/<int:from_year>/to/<int:to_year>')
def get_movie_year(from_year, to_year):
    films = get_movie_by_year(from_year, to_year)
    return films

@app.route('/rating/children')
def get_movie_for_children():
    films = get_movie_by_rating(['G'])
    return films

@app.route('/rating/family')
def get_movie_for_family():
    films = get_movie_by_rating(['G', 'PG', 'PG-13'])
    return films

@app.route('/rating/adult')
def get_movie_for_adult():
    films = get_movie_by_rating(['NC-17', 'R'])
    return films

@app.route('/genre/<genre>')
def get_movie_by_genres(genre):
    films = get_movie_by_genre(genre)
    return films

if __name__ == '__main__':
    app.run(port=5001)