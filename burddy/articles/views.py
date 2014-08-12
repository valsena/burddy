from flask import jsonify

from burddy.utils import template
from burddy.articles import articles
from burddy.extensions import db
from burddy.articles.forms import ArticleForm
from burddy.articles.models import Article


@articles.route('/write', methods=['GET', 'POST'])
@template('articles/editor.html')
def write():
    " give them a rich text editor for the site "
    form = ArticleForm()
    if form.validate_on_submit():
        news = Article(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data
        )
        db.session.add(news)
    return {'form': form}


@articles.route('/popular')
def most_popular():
    """ returns the most popular articles """
    sorted_articles = Article.query.order_by(Article.popularity()).all()
    return jsonify(sorted_articles)
