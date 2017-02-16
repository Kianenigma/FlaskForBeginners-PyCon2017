from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('home.html', title="Home Page")

@app.route('/user')
def user():
    user = {'name': 'kian'}
    return '''
<html>
  <head>
    <title>PyCon</title>
  </head>
  <body>
    <h1>Hello, ''' + user['name'] + '''</h1>
  </body>
</html>
'''

@app.route('/user-template')
def user_template():
    user = {'name': 'kian'}
    title = 'PyCon'
    posts = [
        {
            'author': user,
            'body': 'a mock post'
        },
        {
            'author': user,
            'body': 'another mock post'
        }
    ]
    return render_template('user.html',
    user=user,
    title=title,
    posts=posts
    )
