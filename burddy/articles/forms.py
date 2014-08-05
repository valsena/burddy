from flask.ext.wtf import Form
from wtforms import StringField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import Required, Length

class ArticleForm(Form):
    next = HiddenField()
    title = StringField(validators=[Required()])
    subtitle = StringField(validators=[Required()])
    body = TextAreaField(validators=[Required()])
    submit = SubmitField('Publish')

class CommentForm(Form):
	next = HiddenField()
	text = StringField(validators=[Required(), Length(min=24)])
	submit = SubmitField('Comment')