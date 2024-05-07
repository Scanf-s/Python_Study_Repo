from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators


class UserForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    age = SelectField('나이', choices=[('tens', '10대'), ('twenties', '20대'), ('thirties', '30대'), ('fourties', '40대'),
                                     ('fifties', '50대')], validators=[validators.DataRequired()])
    gender = SelectField('성별', choices=[('male', '남성'), ('female', '여성'), ('other', '그 외')],
                         validators=[validators.DataRequired()])
    submit = SubmitField('검사 시작')
