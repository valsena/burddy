from datetime import datetime
from burddy.extensions import db, login_manager
from burddy.articles.models import Article, Comment

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model):
	" a user of the application "
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True)
	username = db.Column(db.String(64), unique=True)
	password_hash = db.Column(db.String(128))
	joined = db.Column(db.DateTime, default=datetime.utcnow)
	articles = db.relationship('Article', backref='author', lazy='dynamic')
	comments = db.relationship('Comment', backref='comment', lazy='dynamic')

	def __repr__(self):
		return "<username: {}>".format(self.username)