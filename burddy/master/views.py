from flask import render_template

from . import master

@master.route('/')
def home():
    return render_template('home.html')
