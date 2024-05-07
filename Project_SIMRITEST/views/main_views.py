from datetime import datetime

from flask import Blueprint, url_for, render_template
from flask import request, session, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import redirect

from app import db
from forms.Userform import UserForm
from models.model_definitions import UserModel

main_blp = Blueprint('MAIN', __name__, url_prefix='/')


# create user session with user unique id, username
def create_user_session(user_id, user_name):
    session['user_id'] = user_id
    session['username'] = user_name


# get data from form
def get_form_data(form):
    username = form.username.data
    age = form.age.data
    gender = form.gender.data
    return username, age, gender


@main_blp.route('/')
def hello():
    return redirect(url_for('MAIN.index'))


@main_blp.route('/hello')
def index():
    return render_template('home/index.html')


@main_blp.route('/user_info', methods=['GET', 'POST'])
def user_info():
    # use UserForm when POST requests
    # see forms/Userform.py
    user_form = UserForm(request.form)

    # if post request and POST form data is valid
    if request.method == 'POST' and user_form.validate_on_submit():
        username, age, gender = get_form_data(user_form)
        # create UserModel to insert into MySQL database using sqlalchemy
        user = UserModel(
            username=username,
            age=age,
            gender=gender,
            created_at=datetime.now()
        )
        try:
            db.session.add(user)
            db.session.commit()

            create_user_session(user.id, username)
            return redirect(url_for('QUESTION.question_detail', question_id=1))
        except IntegrityError:
            db.session.rollback()
            flash('사용자가 이미 존재합니다.', category="error")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", category="error")
        return redirect(url_for('MAIN.index'))
    # if request == get
    return render_template('home/userinfo.html', form=user_form)


@main_blp.route('/result', methods=['GET'])
def result():
    return render_template('home/result.html')
