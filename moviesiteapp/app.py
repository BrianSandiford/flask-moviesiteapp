import os
import requests
from flask import Flask, render_template, request
from flask_script import Manager
from flask import current_app
#from moviesiteapp import create_app

app = Flask(__name__)
#app.config['DEBUG'] = True
manager = Manager(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/shutdown')
def server_shutdown():
  if not current_app.testing:
     abort(404)
  shutdown = request.environ.get('werkzeug.server.shutdown')
  if not shutdown:
     abort(500)
  shutdown()
  return 'Shutting down...'

@manager.command
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('.')
  unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/', methods=['GET','POST'])
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

if __name__ == '__main__':
    manager.run()

