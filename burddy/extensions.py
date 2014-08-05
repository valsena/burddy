from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask_alembic import Alembic
alembic = Alembic()

flask_ext = [
    db,
    bootstrap,
    login_manager,
    alembic
]
