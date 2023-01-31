#!/usr/bin/env python3
'''
simple flask app
'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    class that has a LANGUAGES class attribute.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE ='en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
bael = Babel(app)


@app.route("/")
def index():
    '''this will be the index page'''
    return render_template("1-index.html")

if __name__ == "__main__":
    app.run()