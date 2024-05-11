from flask import session, redirect, url_for, flash, request

from config.db import db
from models.model_definitions import QuestionModel, AnswerModel


def get_questions():
    """
    Function to get all question
    :return: questions
    """
    questions = QuestionModel.query.filter_by(is_active=True).order_by(QuestionModel.order_num.asc()).all()
    return questions


def get_form_data(form):
    """
    Function to get form data
    Returns answer data that user answered
    :param form:
    :return: answer
    """
    answer = form.answer.data
    return answer


def get_session_info():
    """
    Function to get session info
    :return: Session data dictionary
    """
    return {
        "answered_user_id": session.get('user_id', None),
        "answered_username": session.get('username', None)
    }


def redirect_next_question(current_question_order_num, session_info):
    """
    Function to get the next question
    :param current_question_order_num:
    :param session_info:
    :return:
    """
    if session_info and current_question_order_num < len(get_questions()):
        return redirect(url_for('QUESTION.question_detail', question_order_num=current_question_order_num + 1))
    else:
        return redirect(url_for('QUESTION.question_result'))


def verify_question_order_num(question_order_num):
    """
    verify if requested order number is valid
    order number has to be between 1 and len(questions)
    :param question_order_num:
    :return: Question or redirect
    """
    questions = get_questions()
    if 1 <= question_order_num <= len(questions):
        return questions[question_order_num - 1]
    else:
        flash("Invalid question order number", category="error")
        return False


def insert_answer_in_database(answer_data, session_info, question_id):
    """
    Function to create new answer
    :param answer_data: Data of the answer to insert
    :param session_info: Session information containing user details
    :param question_id: ID of the question being answered
    :return: Boolean indicating success or failure
    """

    # verify user has session info and is authenticated
    if not session_info.get('answered_username') or not session_info.get('answered_user_id'):
        flash("Please enter your information", category="warning")
        return redirect(url_for('MAIN.index'))

    answer = AnswerModel(
        user_id=session_info['answered_user_id'],
        question_id=question_id,
        chosen_answer=answer_data
    )

    existing_answer = AnswerModel.query.filter_by(user_id=session_info['answered_user_id'], question_id=question_id).first()
    if existing_answer is None:
        db.session.add(answer)
        db.session.commit()
        return True
    else:
        # if user already answered question, return True to redirect next question
        return True
