from datetime import datetime
from burddy.extensions import db

class Article(db.Model):
    """ database representation of an article """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    subtitle = db.Column(db.String(512))
    body = db.Column(db.Text())
    votes = db.Column(db.Integer, default=1)
    views = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def popularity(self, gravity=1.8):
        """ uses hacker news popularity rating """
        submit_delta = (self.timestamp - datetime.utcnow()).total_seconds()
        time_decay = submit_delta / 120
        popularity = (self.views - 1) / (time_decay + 2) ** gravity
        return popularity

    def __repr__(self):
        return '{}\n{}\n{}\n'.format(self.title, self.subtitle, self.body)
