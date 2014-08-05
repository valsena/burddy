from flask import Blueprint

user = Blueprint('user', __name__)

@user.record_once
def register(state):
	from burddy.user import views
	from burddy.user.commands import cli

	state.app.cli.add_command(cli, 'user')