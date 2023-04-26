from flask import Flask
from markupsafe import escape
from flask import url_for

app=Flask(__name__)

@app.route('/user/<name>')
def hello(name):
    return f'User:{escape(name)}'

@app.route('/')
def nihao():
    return '<h1>hello</h1>'

@app.route('/test')
def test():
    print(url_for('hello',name='jack'))
    print(url_for('nihao'))
    return 'test page'