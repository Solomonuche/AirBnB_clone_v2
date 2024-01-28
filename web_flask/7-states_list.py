#!/usr/bin/python3
""" a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """ Perform clean up after request"""

    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ render list states"""

    obj = storage.all(State)
    states = []
    for values in obj.values():
        states.append(values)

    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
