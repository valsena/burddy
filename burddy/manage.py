import click
from flask.cli import FlaskGroup
from burddy.extensions import db
from burddy import create_app


cli = FlaskGroup(create_app=create_app)

@cli.command()
def initdb():
    """ create the database """
    db.drop_all()
    db.create_all()


@cli.command()
@click.option('--count', default=100, type=int)
@click.pass_context
def seed(ctx, count):
    """ make a fake populated website """
    from burddy.articles.commands import seed as seed_articles

    ctx.invoke(seed_articles)

    click.echo('finished seeding the database')


if __name__ == '__main__':
    cli()
