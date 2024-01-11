#!/usr/bin/env python3
"""
Module documentation: 2-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel()


class Config:
    """
    Config class documentation
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Move the definition of get_locale before init_app
@babel.localeselector
def get_locale():
    """
    Locale selector documentation
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route('/')
def index():
    """
    Route documentation: /
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
