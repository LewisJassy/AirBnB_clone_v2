#!/usr/bin/python3
"""script to start a flask app on localhost
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)