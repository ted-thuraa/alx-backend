#!/usr/bin/env python3
'''
simple flask app
'''
from flask import Flask, render_template, request
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
    return render_template("2-index.html")

@babel.localeselector
def get_locale():
    """select best lang match"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

if __name__ == "__main__":
    app.run()