#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Config for languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """
    Return index
    """
    return render_template('4-index.html')


@app.before_request
def get_locale():
    supported_locales = ['en', 'fr']
    if 'locale' in request.args and request.args['locale'] in supported_locales:
        return request.args['locale']
    # Si el argumento 'locale' no está presente o no es compatible, se utiliza el comportamiento predeterminado.
    return request.accept_languages.best_match(supported_locales)
