import os
from sys import stderr
from flask import Flask, render_template
from flask_alembic.cli.click import cli as alembic_cli

from burddy.extensions import flask_ext

__all__ = ['create_app']

def create_app(info=None):
    " create the application in the proper context "
    app = Flask(__name__, instance_relative_config=True)
    print(app.instance_path, file=stderr)
    app.config.from_object('burddy.config.defaults')
    app.config.from_pyfile('config.py', True)

    app.cli.add_command(alembic_cli, 'db')

    configure_blueprints(app)
    configure_errorhandlers(app)
    configure_extensions(app)

    return app


def configure_blueprints(app):
    " configure the blueprints with the application "
    from burddy.master import master
    from burddy.articles import articles
    from burddy.user import user

    app.register_blueprint(master)
    app.register_blueprint(articles, url_prefix='/article')
    app.register_blueprint(user, url_prefix='/user')


def configure_extensions(app):
    " put flask extensions on the application "
    for extension in flask_ext:
        extension.init_app(app)


def configure_errorhandlers(app):
    " puts the HTTP error handlers on the app "

    @app.errorhandler(404)
    def not_found(e):
        return render_template('errors/404.html')
