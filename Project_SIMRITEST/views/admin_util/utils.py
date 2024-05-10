from models.model_definitions import QuestionModel
from flask import flash, redirect, url_for
from config.db import db


def get_admin_form_data(form):
    username = form.username.data
    password = form.password.data
    return username, password


def get_admin_register_form_data(form):
    username = form.username.data
    email = form.email.data
    password = form.password.data
    return username, email, password


def get_question_form_data(form):
    content = form.content.data
    order_num = form.order_num.data
    is_active = form.is_active.data
    return content, order_num, is_active


def insert_question_in_database(question_form):
    """
    Function to insert a question into the database
    :param question_form:
    :return:
    """
    if question_form.validate_on_submit():
        content, order_num, is_active = get_question_form_data(question_form)
        new_question = QuestionModel(
            content=content,
            order_num=order_num,
            is_active=is_active
        )
        db.session.add(new_question)
        db.session.commit()
        flash("Successfully added question", "success")
        return redirect(url_for('admin.add_question'))
