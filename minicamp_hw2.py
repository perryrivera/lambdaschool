# First two lines of any flask app follow...

from flask import Flask, render_template

app = Flask(__name__)

# When somebody hits this route, return home.html...
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def about():
    return 'July 12 1814'

@app.route('/greeting/<name>')
def greet(name):
    return 'Hello %s' % name

    
