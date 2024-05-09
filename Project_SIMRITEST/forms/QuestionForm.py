from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators


class QuestionForm(FlaskForm):
    content = StringField('질문 입력', validators=[validators.DataRequired()])
    submit = SubmitField('추가')
