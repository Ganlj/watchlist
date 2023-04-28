from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template

app=Flask(__name__)

name = 'Lin jun'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/user/<name>')
def hello(name):
    return f'User:{escape(name)}'

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/test')
def test():
    print(url_for('hello',name='jack'))
    print(url_for('nihao'))
    return 'test page'