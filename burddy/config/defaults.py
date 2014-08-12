from os import urandom

PROJECT_NAME = 'Burddy'
DEBUG = True
SECRET_KEY = urandom(24)
SQLALCHEMY_DATABASE_URI = 'postgresql:///burddy'
