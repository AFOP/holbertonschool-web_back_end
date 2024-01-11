#!/usr/bin/env python3
"""
Module documentation: 2-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)

class Config:
    """
    Config class documentation
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Elimina la instancia de Babel en el nivel del módulo
# babel = Babel(app)

app.config.from_object(Config)

# Mueve la definición de get_locale antes de la llamada a init_app
@babel.localeselector
def get_locale():
    """
    Locale selector documentation
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    """
    Route documentation: /
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
