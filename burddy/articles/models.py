from flask.ext.login import current_user
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy import func

from burddy.extensions import db

class Article(db.Model):
    " database representation of an article "
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    subtitle = db.Column(db.String(512))
    body = db.Column(db.Text())
    views = db.Column(db.Integer, default=1)
    category = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    visited_users = db.Column(db.PickleType())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @hybrid_method
    def popularity(self, gravity=1.8):
        seconds = (self.timestamp - datetime.utcnow()).total_seconds()
        hours = seconds / 3600
        return (self.views - 1) / (hours + 2) ** gravity

    @popularity.expression
    def popularity(self, gravity=1.8):
        seconds = func.extract('epoch', self.timestamp - func.now())
        hours = seconds / 3600
        return (self.views - 1) / func.power((hours + 2), gravity)

    def __repr__(self):
        return '{}\n{}\n{}\n'.format(self.title, self.subtitle, self.body)


class Comment(db.Model):
    " a comment on an article "
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    disabled = db.Column(db.Boolean, default=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    def __repr__(self):
        return "{}\n(authored by: {} at {})".format(html, author.username, timestamp)
