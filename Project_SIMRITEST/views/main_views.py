from datetime import datetime

from flask import request, session, flash

from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
from sqlalchemy.exc import IntegrityError

from app import db
from models.model_definitions import UserModel

main_blp = Blueprint('MAIN', __name__, url_prefix='/')


@main_blp.route('/')
def hello():
    return redirect(url_for('MAIN.index'))


@main_blp.route('/hello')
def index():
    return render_template('home/index.html')

@main_blp.route('/user_info', methods=['GET', 'POST'])
def user_info():
    # get form data from userinfo.html
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        gender = request.form['gender']

        # make UserModel to insert mysql database
        user = UserModel(
            username=username,
            age=age,
            gender=gender,
            created_at=datetime.now()
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('사용자가 이미 존재합니다.', category="error")
            return redirect(url_for('MAIN.index'))
        except Exception as e:
            flash("Error : {}".format(e), category="error")
            return redirect(url_for("MAIN.index"))

        # Create a session to remember who is answering questions
        session['user_id'] = user.id
        session['username'] = username

        # pass question_id=1 to start the first question
        return redirect(url_for('QUESTION.question_detail', question_id=1))

    # if request.method ==' GET'
    return render_template('home/userinfo.html')


@main_blp.route('/result')
def result():
    return render_template('home/result.html')
