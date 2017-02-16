from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
<<<<<<< HEAD
from flask import redirect
=======
>>>>>>> ff6c0ef348a3cad698ed2dc8af899608260fa58b
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('request',request)
    print('method', request.method)
    print('form', request.form)
    print('args', request.args)
<<<<<<< HEAD
    
    # interesting to see later
    # print('headers', request.headers)

    if request.method == 'POST':
        return jsonify(status='ok')
    elif request.method == 'GET':
        return render_template('login.html')
        # return redirect("/")
=======

    if request.method == 'POST':
        return jsonify('ok')
    elif request.method == 'GET':
        return render_template('login.html')
>>>>>>> ff6c0ef348a3cad698ed2dc8af899608260fa58b
    else:
        abort(404)
