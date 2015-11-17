# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

def uppercase(name):
    return name.upper()

@app.route('/')
def index():
    return 'Hello!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + uppercase(name)

if __name__ == '__main__':
    app.run(port=9000, debug=True)
