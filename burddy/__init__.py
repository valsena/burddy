from flask import Flask
from flask import render_template
from flask_alembic.cli.click import cli as alembic_cli

from burddy.extensions import flask_ext

__all__ = ['create_app']

def create_app(info=None):
    """ create the app with a config """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('burddy.config.defaults')
    app.config.from_pyfile('user.cfg', True)

    configure_blueprints(app)
    configure_errorhandlers(app)
    configure_extensions(app)

    return app


def configure_blueprints(app):
    """ configure the blueprints with the application """
    from burddy.master import master
    from burddy.articles import articles

    app.register_blueprint(master)
    app.register_blueprint(articles, url_prefix='/article')


def configure_extensions(app):
    """ put flask extensions on the application """
    for extension in flask_ext:
        extension.init_app(app)


def configure_errorhandlers(app):
    """ puts the HTTP error handlers on the app """

    @app.errorhandler(404)
    def not_found(e):
        return render_template('errors/404.html')
