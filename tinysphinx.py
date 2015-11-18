# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

def uppercase(name):
    '''Uppercase a name

    Example:

        .. code-block:: python

            print uppercase('ben')
            # 'BEN'

    Arguments:
        name (str): a name

    Returns:
        str: The name, uppercased
    '''
    return name.upper()

@app.route('/')
def index():
    '''Render the home screen

    :status 200: Successfully render
    :status 404: Not found
    '''
    return 'Hello!'

@app.route('/hello/<name>')
def hello(name):
    '''Say hi to a name

    :param name: The name to say hi to
    :status 200: Say hi to the name!
    '''
    return 'Hello, ' + uppercase(name)

if __name__ == '__main__':
    app.run(port=9000, debug=True)
