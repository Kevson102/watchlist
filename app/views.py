from flask import render_template
from app import app
from .request import get_movies, get_movie


# Views

@app.route('/')
def index():
    '''
    View root page functions that returns the index page and its data
    '''
    # Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    # print (popular_movies)
    title = "Home - welcome to the best Movie Review Website Online"
    return render_template('index.html', title=title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)


@app.route('/movie/<int:id>')
def movie(id):
    '''
    view movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title=title, movie=movie)