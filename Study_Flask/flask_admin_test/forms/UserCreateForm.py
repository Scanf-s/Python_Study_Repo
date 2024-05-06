from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
