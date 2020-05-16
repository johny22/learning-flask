from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello, Jones!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/') # It's better to use thus, see the comment in the next function
def projects():
    return 'The project page'

@app.route('/about') # /about/ will raise 404
def about():
    return 'The about page'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='j.r.bezerra', next='/'))