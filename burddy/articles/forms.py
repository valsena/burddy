from flask.ext.wtf import Form
from wtforms import StringField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import Required

class ArticleForm(Form):
    next = HiddenField()
    title = StringField(validators=[Required()])
    subtitle = StringField(validators=[Required()])
    body = TextAreaField(validators=[Required()])
    submit = SubmitField('Publish')
