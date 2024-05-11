from datetime import datetime

from flask import flash, redirect, url_for

from config.db import db
from models.model_definitions import QuestionModel, AdminModel


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


def insert_admin_in_database(admin_register_form):
    """
    Function to insert an admin data into the database
    :param admin_register_form: admin register data [request.form] required!!
    :return:
    """
    username, email, password = get_admin_register_form_data(admin_register_form)
    flash(f"username : {username}, email:{email}, password:{password}", "success")
    admin = AdminModel(
        username=username,
        email=email,
        is_admin=True,
        created_at=datetime.now()
    )
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    return True


def update_activation(update_target_ids, set_activate_status):
    """
    update is_active status in QuestionModel
    :param update_target_ids:
    :param set_activate_status: if set_activate_status is 1 then is_active = True else set_activate_status is 0 then is_active = False
    :return:
    """
    # https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.ColumnOperators.in_
    target_metadata_list = QuestionModel.query.filter(QuestionModel.id.in_(update_target_ids))
    if set_activate_status == 1:
        for target_metadata in target_metadata_list:
            target_metadata.is_active = True
        flash("Activated checked questions.", category="success")
    elif set_activate_status == 0:
        for target_metadata in target_metadata_list:
            target_metadata.is_active = False
        flash("Deactivated checked questions.", category="success")
    else:
        flash("Wrong activation status.", category="error")
    db.session.commit()


def delete_questions_in_database(update_target_ids):
    """
    delete questions in QuestionModel
    :param update_target_ids:
    :return:
    """
    # https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.ColumnOperators.in_
    QuestionModel.query.filter(QuestionModel.id.in_(update_target_ids)).delete()
    db.session.commit()
    flash("Deleted checked questions.", category="success")