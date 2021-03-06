import click
from burddy.extensions import db
from burddy.utils import get_random
from burddy.articles.models import Article, Comment
from burddy.user.models import User
from random import seed, randint

@click.group()
def cli():
    " manage the articles "
    pass


@cli.command()
@click.option('-c', '--count', default=100)
def seed(count):
    " make some fake articles "
    import forgery_py as f

    seed()
    for i in range(count):
        a = Article(
            title=f.lorem_ipsum.title(),
            subtitle=f.lorem_ipsum.title(),
            body=f.lorem_ipsum.paragraph(html=True, sentences_quantity=100),
            author=get_random(User)
        )
        db.session.add(a)
        db.session.commit()
    click.echo('added {} articles to the database'.format(Article.query.count()))
