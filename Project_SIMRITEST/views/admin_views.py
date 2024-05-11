from flask import request, redirect, url_for, render_template, Blueprint, flash
from flask_login import login_user, logout_user
from flask_paginate import Pagination, get_page_parameter
from werkzeug.security import check_password_hash

from forms.AdminForm import AdminForm, AdminRegisterForm
from forms.QuestionForm import QuestionForm
from models.model_definitions import AdminModel, AnswerModel, QuestionModel
from views.admin_util.utils import (
    get_admin_form_data,
    insert_question_in_database,
    insert_admin_in_database,
    update_activation,
    delete_questions_in_database
)

admin_blp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blp.route('/register', methods=["GET", "POST"])
# This method is very dangerous for security,
# but it has been implemented for convenience of development.
def register():
    """
    Route function that registers a new user
    :return: redirects to /admin/register or render template register.html
    """
    admin_register_form = AdminRegisterForm(request.form)
    # If the user fills the form and makes a POST request
    if request.method == "POST" and admin_register_form.validate_on_submit():
        if insert_admin_in_database(admin_register_form):
            # Once an admin account created, redirect him/her to login route
            return redirect(url_for("admin.login"))
    # Renders sign_up template if user made a GET request
    return render_template("admin/register.html", form=admin_register_form)


@admin_blp.route("/login", methods=["GET", "POST"])
def login():
    admin_form = AdminForm(request.form)

    if request.method == "POST" and admin_form.validate_on_submit():
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

    # if request == GET
    return render_template("admin/admin_login.html", form=admin_form)


@admin_blp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("admin.home"))


@admin_blp.route("/answer_list", methods=["GET"])
def answer_list():
    # pagination config
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    offset = (page - 1) * per_page
    total = AnswerModel.query.count()

    answers = AnswerModel.query.order_by(AnswerModel.user_id.asc()).offset(offset).limit(per_page).all()
    pagination = Pagination(page=page, total=total, per_page=per_page, record_name='answers')
    return render_template("admin/answer_list.html", answers=answers, pagination=pagination)


@admin_blp.route("/question_list", methods=["GET"])
def question_list():
    # pagination config
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # Amount of content to show on a page
    offset = (page - 1) * per_page
    # Depending on the current page, we need to determine the starting location to import from the database.
    # For example, the starting position of the DB displayed on page 1 is zero
    # The starting position of the DB displayed on page 2 is 10
    total = QuestionModel.query.count()  # Total amount of content to page-nation

    # Query based on Ordernum ascending order in QuestionModel,
    # set the start position to offset and import only per_page
    questions = QuestionModel.query.order_by(QuestionModel.order_num.asc()).offset(offset).limit(per_page).all()
    pagination = Pagination(page=page, total=total, per_page=per_page, record_name='questions')
    return render_template(
        "admin/question_list.html",
        questions=questions,
        pagination=pagination,
        form=QuestionForm(),
    )


@admin_blp.route("/add_question", methods=["GET", "POST"])
def add_question():
    # use UserForm when POST requests
    # see forms/Userform.py
    question_form = QuestionForm(request.form)

    # if post request and POST form data is valid
    if request.method == 'POST':
        insert_question_in_database(question_form)
        return redirect(url_for('admin.add_question'))

    # if request == get
    return render_template('admin/add_question.html', form=question_form)


@admin_blp.route("/update_questions", methods=["POST"])
def update_questions():
    """
    Route function that updates questions
    :return:
    """

    # if delete request
    if request.form.get("delete_row_data") == "delete":
        update_target_ids = request.form.getlist("question_checkbox")
        delete_questions_in_database(update_target_ids)
        return redirect(url_for("admin.question_list"))

    # if update to set activate request
    elif request.form.get("activate_status") == "activate":
        update_target_ids = request.form.getlist("question_checkbox")
        update_activation(update_target_ids, 1)
        return redirect(url_for("admin.question_list"))

    # if update to set deactivate request
    elif request.form.get("deactivate_status") == "deactivate":
        update_target_ids = request.form.getlist("question_checkbox")
        update_activation(update_target_ids, 0)
        return redirect(url_for("admin.question_list"))

    return redirect(url_for("admin.question_list"))


@admin_blp.route("/")
def home():
    return render_template("admin/admin_home.html")
