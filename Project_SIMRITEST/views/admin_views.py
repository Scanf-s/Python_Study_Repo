from datetime import datetime

from flask import request, redirect, url_for, render_template, Blueprint, flash
from flask_login import login_user, logout_user
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from views.admin_util.utils import (
    get_admin_form_data,
    get_question_form_data
)
from app import db
from forms.AdminForm import AdminForm, AdminRegisterForm
from forms.QuestionForm import QuestionForm
from models.model_definitions import AdminModel, AnswerModel, QuestionModel

admin_blp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blp.route('/register', methods=["GET", "POST"])
# This method is very dangerous for security,
# but it has been implemented for convenience of development.
def register():
    # If the user made a POST request, create a new user
    admin_form = AdminRegisterForm(request.form)
    if request.method == "POST" and admin_form.validate_on_submit():
        admin = AdminModel(
            username=admin_form.username.data,
            email=admin_form.email.data,
            is_admin=True,
            created_at=datetime.now()
        )
        password = admin_form.password.data
        admin.set_password(password)

        try:
            db.session.add(admin)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            flash("There are duplicate elements in database. Please use another username or email", "error")
            return redirect(url_for('admin.register'))
        except Exception as e:
            db.session.rollback()
            flash("Error : {}".format(e), category="error")
            return redirect(url_for("admin.register"))

        # Once a user account created, redirect them to login route
        return redirect(url_for("admin.login"))
    # Renders sign_up template if user made a GET request
    return render_template("admin/register.html", form=admin_form)


@admin_blp.route("/login", methods=["GET", "POST"])
def login():
    # use AdminForm when POST requests
    # see forms/AdminForm.py
    admin_form = AdminForm(request.form)

    if request.method == "POST" and admin_form.validate_on_submit():
        try:
            username, password = get_admin_form_data(admin_form)
            admin = AdminModel.query.filter_by(username=username).first()

            # Password in requested form data,
            # check if form password hash code is in AdminModel
            if admin and check_password_hash(admin.password_hash, password):
                # Use the login_user method to log in the user
                login_user(admin)
                flash("You are logged in.", category="success")
                return redirect(url_for("admin.home"))
            else:
                flash("Incorrect password.", category="error")
                return redirect(url_for("admin.login"))
        except AttributeError:
            flash(f"username : {request.form.get("username")} not exist", category="error")
            return redirect(url_for("admin.login"))
        except Exception as e:
            flash("Error : {}".format(e), category="error")
            return redirect(url_for("admin.login"))

    # if request == GET
    return render_template("admin/admin_login.html", form=admin_form)


@admin_blp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("admin.home"))


@admin_blp.route("/answer_list", methods=["GET"])
def answer_list():
    # PageNation function to be implemented in the future
    answers = AnswerModel.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(answers), record_name='answers', per_page=10)
    return render_template("admin/answer_list.html", answers=answers, pagination=pagination)


@admin_blp.route("/question_list", methods=["GET"])
def question_list():
    questions = QuestionModel.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination = Pagination(page=page, total=len(questions), record_name='questions', per_page=10)
    return render_template("admin/question_list.html", questions=questions, pagination=pagination)


@admin_blp.route("/add_question", methods=["GET", "POST"])
def add_question():
    # use UserForm when POST requests
    # see forms/Userform.py
    question_form = QuestionForm(request.form)

    # if post request and POST form data is valid
    if request.method == 'POST' and question_form.validate_on_submit():
        content, order_num, is_active = get_question_form_data(question_form)
        # create UserModel to insert into MySQL database using sqlalchemy
        new_question = QuestionModel(
            content=content,
            order_num=order_num,
            is_active=is_active
        )
        try:
            db.session.add(new_question)
            db.session.commit()

            return redirect(url_for('admin.add_question'))
        except IntegrityError as ie:
            db.session.rollback()
            flash(f"Error: {ie}", category="error")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", category="error")
        return redirect(url_for('admin.add_question'))

    # if request == get
    return render_template('admin/add_question.html', form=question_form)




@admin_blp.route("/")
def home():
    return render_template("admin/admin_home.html")
