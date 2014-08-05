from burddy.extensions import db

class Article(db.Model):
    """ database representation of an article """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    subtitle = db.Column(db.String(512))
    body = db.Column(db.Text())

    @staticmethod
    def top_stories():
        """ find the most appealing stories written """
        pass

    def __repr__(self):
        return '{}\n{}\n{}\n'.format(self.title, self.subtitle, self.body)
