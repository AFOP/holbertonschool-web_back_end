#!/usr/bin/env python3
"""
Module documentation: 3-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _  # Importar la función de traducción

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
babel.init_app(app)

@babel.localeselector
def get_locale():
    """
    Locale selector documentation
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Route documentation: /
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
