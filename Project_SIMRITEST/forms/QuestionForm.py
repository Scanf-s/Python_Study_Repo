from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, validators


class QuestionForm(FlaskForm):
    content = StringField('질문 입력', validators=[validators.DataRequired()])
    order_num = IntegerField('질문 번호', validators=[validators.DataRequired()])
    is_active = BooleanField('활성화', validators=[validators.DataRequired()])
    submit = SubmitField('추가')
