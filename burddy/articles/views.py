from flask import render_template

from burddy.extensions import db
from .forms import ArticleForm
from .models import Article
from . import articles


@articles.route('/write', methods=['GET', 'POST'])
def write():
    """ Render the rich text editor for editing """
    form = ArticleForm()
    if form.validate_on_submit():
        news = Article(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data
        )
        print(news)
        db.session.add(news)
    return render_template('articles/editor.html', form=form)


@articles.route('/popular')
def most_popular():
    """ returns the most popular articles """
    sorted_articles = Article.query.order_by(popularity()).all()
    return jsonify([x.popularity() for x in sorted_articles])