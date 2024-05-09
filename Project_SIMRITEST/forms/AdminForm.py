from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class AdminForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('로그인')
