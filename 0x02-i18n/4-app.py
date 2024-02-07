#!/usr/bin/env python3
"""force locale with url parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask App"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Users from flask request"""
    locale = request.args.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
