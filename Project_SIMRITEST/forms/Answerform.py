from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    answer = RadioField('Answer', choices=[('yes', '네'), ('no', '아니오')], validators=[DataRequired()])
    submit = SubmitField('다음')
