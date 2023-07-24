#!/usr/bin/python3

"""
Flask Web Application

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines a single route that displays "Hello HBNB!" when accessed.

Routes:
    /: Display "Hello HBNB!"

Usage:
    Run this script and visit http://0.0.0.0:5000/ in your web browser.

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the webpage."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
