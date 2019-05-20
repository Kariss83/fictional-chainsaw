from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = StringField('What do you want to say to GrandPy?',
        validators=[DataRequired()])
    submit = SubmitField('Send')
