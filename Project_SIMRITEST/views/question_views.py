from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask import request
from sqlalchemy.exc import IntegrityError

from app import db
from forms.Answerform import AnswerForm
from models.model_definitions import QuestionModel, AnswerModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


def get_questions():
    """
    Function to get all questions
    :return:
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
    :return: session_info
    """
    answered_user_id = session.get('user_id', None)
    answered_username = session.get('username', None)
    session_info = {
        "answered_user_id": answered_user_id,
        "answered_username": answered_username
    }
    return session_info


def get_next_question(current_question_order_num, session_info):
    """
    Function to get next question
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
    if question order number is less than or equal to 5,
    then return question from database. Otherwise, redirect to result.
    :param question_order_num:
    :return: question or redirect
    """
    try:
        if 1 <= question_order_num <= 5:
            questions = get_questions()
            question = questions[question_order_num - 1]
            return question
        else:
            flash("Invalid question number", category="error")
            return redirect(url_for('QUESTION.question_result'))
    except IndexError as e:
        flash(f'Error: {e}', 'error')
        return redirect(url_for('MAIN.index'))
    except Exception as e:
        flash(f'Error: {e}', 'error')
        return redirect(url_for('MAIN.index'))


@question_blp.route('/result', methods=['GET'])
def question_result():
    session_info = get_session_info()
    flash('검사 완료', category="success")
    session.pop('user_id', None)
    answers = AnswerModel.query.filter_by(user_id=session_info['answered_user_id']).order_by(
        AnswerModel.id.asc()).all()
    return render_template('question/result.html', answered_user=session_info['answered_username'], answers=answers)


@question_blp.route('/detail/<int:question_order_num>/', methods=['GET', 'POST'])
def question_detail(question_order_num):
    # get session info to verify current user is valid
    session_info = get_session_info()

    # get question if question order number less than 5
    question = verify_question_order_num(question_order_num)

    # use AnswerForm when POST requests
    # see forms/Answerform.py
    answer_form = AnswerForm(request.form)

    # if there is no session info, redirect to user_info page
    if not session_info['answered_username']:
        flash("Please enter your information", category="warning")
        return redirect(url_for('MAIN.user_info'))

    if request.method == 'POST' and answer_form.validate_on_submit():
        answer = get_form_data(answer_form)

        # if current user has session(cookie)
        if session_info:
            answer = AnswerModel(
                user_id=session_info['answered_user_id'],
                question_id=question.id,
                chosen_answer=answer_form.answer.data
            )
            try:
                db.session.add(answer)
                db.session.commit()
                return get_next_question(question_order_num, session_info)
            except IntegrityError:
                db.session.rollback()
                flash('Integrity Error Occurs.', category="error")
            except Exception as e:
                db.session.rollback()
                flash(f"Error: {e}", category="error")
            return redirect(url_for('MAIN.index'))

    # if request.method == 'GET', just render question_detail page
    return render_template('question/question_detail.html', question_order_num=question_order_num, question=question,
                           form=answer_form)
