#!/usr/bin/python3
""" a script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("__init__.py")


@app.route("/", strict_slashes=False)
def display():
    """ Display Hello HBNB!"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display Hello HBNB!"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def var_C(text):
    """ Display Hello HBNB!"""

    if "_" in text:
        text = text.replace("_", " ")

    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def var_python(text="is cool"):
    """ Display Hello HBNB!"""

    if "_" in text:
        text = text.replace("_", " ")

    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def var_number(n):
    """ Display Hello HBNB!"""

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ return rendered template"""

    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
