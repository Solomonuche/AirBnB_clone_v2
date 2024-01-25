#!/usr/bin/python3
""" a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("__init__.py")


@app.route("/", strict_slashes=False)
def display():
    """ Display Hello HBNB!"""

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
