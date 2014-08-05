import click
from burddy.extensions import db
from burddy.utils import get_random
from burddy.articles.models import Article, Comment
from burddy.user.models import User
from random import seed, randint

@click.group()
def cli():
    " manage the users "
    pass


@cli.command()
@click.option('-c', '--count', default=100)
def seed(count):
    " adds fake users to database "
    import forgery_py as f
    from sqlalchemy.exc import IntegrityError

    seed()
    for i in range(count):
        fake_user = User(
            email=f.internet.email(),
            username=f.internet.username()
        )
        try:
            db.session.add(fake_user)
        except IntegrityError:
            db.session.rollback(fake_user)
        db.session.commit()
    click.echo('added {} articles to the database'.format(Article.query.count()))