from flask import Blueprint

articles = Blueprint('articles', __name__)

@articles.record_once
def register(state):
    from burddy.articles import views
    from burddy.articles.commands import cli

    state.app.cli.add_command(cli, 'article')
