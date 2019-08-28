from flask import render_template, request
from app import app

# @app.route('/index')
@app.route('/query')
# def index():
#     # return 'qwerty'
#     return flask.render_template('priority_price.html');

@app.route('/')
def foo():
    print(request.args.get('x'))
    print(request.args.get('y'))