import click
from burddy.extensions import db
from burddy.articles.models import Article

@click.group()
def cli():
    """ manage the articles """
    pass


@cli.command()
@click.option('-c', '--count', default=100, help='create some fake articles')
def seed(count):
    from random import seed
    import forgery_py as f

    seed()
    for i in range(count):
        a = Article(
            title=f.lorem_ipsum.title(),
            subtitle=f.lorem_ipsum.title(),
            body=f.lorem_ipsum.paragraph(html=True, sentences_quantity=100)
        )
        db.session.add(a)
        db.session.commit()
    click.echo('added {} articles to the database'.format(Article.query.count()))


@cli.command()
@click.argument('article_id')
def get_popularity(article_id):
    a = Article.query.get(article_id)
    click.echo('"{}" has a popularity of {}'.format(a.title, a.popularity()))
