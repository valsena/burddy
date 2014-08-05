from flask import Blueprint

master = Blueprint('master', __name__)

@master.record_once
def register(state):
    from . import views
