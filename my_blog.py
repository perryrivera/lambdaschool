# First two lines of any flask app follow...

from flask import Flask

app = Flask(__name__)

# When somebody hits this route, return home.html...
@app.route('/')
def index():
    return app.send_static_file('home.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/post/<postnum>')
def post1(postnum):
    return 'This is post %s' % postnum
