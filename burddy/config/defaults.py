from os.path import join as osjoin, dirname as osdir, abspath as osabs
from os import urandom

PROJECT_NAME = 'Burddy'
DEBUG = True
SECRET_KEY = urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + osabs(osjoin(osdir(__file__), '../data.sqlite'))
