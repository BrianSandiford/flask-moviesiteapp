import os
import requests
from flask import render_template, session, redirect, url_for, current_app, request, abort
from . import main

@main.route('/shutdown')
def server_shutdown():
  if not current_app.testing:
     abort(404)
  shutdown = request.environ.get('werkzeug.server.shutdown')
  if not shutdown:
     abort(500)
  shutdown()
  return 'Shutting down...'

@main.route('/', methods=['GET', 'POST'])
def index():
    api_key =  os.getenv('SECRET_KEY')
    if request.method == 'POST' :
        movie_name = request.form.get('movie_name')
        if movie_name:
             url = 'https://api.themoviedb.org/3/search/movie?api_key={}'.format(api_key) +'&language=en-US&query={}&page=1&include_adult=false'
             r = requests.get(url.format(movie_name)).json()
        else:
          url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
          r = requests.get(url).json()
    else:
      url = 'https://api.themoviedb.org/3/movie/popular?api_key={}'.format(api_key) +'&language=en-US&page=1'
      r = requests.get(url).json()
    if not r['results']:
      return render_template('404.html'), 404
    else:
     return  render_template('index.html', data=r['results'])