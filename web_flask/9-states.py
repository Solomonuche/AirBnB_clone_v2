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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ render list states"""

    if id:
        Obj = storage.all(State).get(id)
        return render_template('9-states.html', Obj=Obj)
    else:
        return render_template(
                '9-states.html', storage=storage.all(State))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
