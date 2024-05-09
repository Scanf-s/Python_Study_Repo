from flask import session, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError

from config.db import db
from models.model_definitions import QuestionModel, AnswerModel


def get_questions():
    """
    Function to get all question
    :return: questions
    """
    questions = QuestionModel.query.filter_by(is_active=True).limit(5).all()
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
    if current_question_order_num < 5:
        return redirect(url_for('QUESTION.question_detail', question_order_num=current_question_order_num + 1))
    else:
        # After the 5th question, redirect to the result page
        return redirect(url_for('QUESTION.question_result'))


def verify_question_order_num(question_order_num):
    """
    Verify the question order number
    This app shows up to 5 questions.
    if the question order number is less than or equal to 5,
    then return question from a database. Otherwise, redirect to result.
    :param question_order_num:
    :return: question or redirect
    """
    try:
        questions = get_questions()
        if 1 <= question_order_num <= len(questions):
            return questions[question_order_num - 1]
        else:
            flash("Invalid question order number", category="error")
            return redirect(url_for('QUESTION.question_result'))
    except IndexError as e:
        flash(f'Error: {e}', 'error')
        return redirect(url_for('MAIN.index'))
    except Exception as e:
        flash(f'Error: {e}', 'error')
        return redirect(url_for('MAIN.index'))


def write_answer_in_database(answer_data, session_info, question_id):
    """
    Function to create new answer
    :param answer_data:
    :param session_info:
    :param question_id:
    :return:
    """

    # verify user has session info
    if not session_info['answered_username']:
        flash("Please enter your information", category="warning")
        return False

    answer = AnswerModel(
        user_id=session_info['answered_user_id'],
        question_id=question_id,
        chosen_answer=answer_data
    )
    try:
        db.session.add(answer)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'error')
        return False
