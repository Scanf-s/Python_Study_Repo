from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask import request
from sqlalchemy.exc import IntegrityError

from app import db
from forms.Answerform import AnswerForm
from models.model_definitions import QuestionModel, AnswerModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


def get_from_data(form):
    answer = form.answer.data
    return answer


def get_session_info():
    answered_user_id = session.get('user_id', None)
    answered_username = session.get('username', None)
    session_info = {
        "answered_user_id": answered_user_id,
        "answered_username": answered_username
    }
    return session_info


def get_next_question(current_question_id, session_info):
    # filter only questions that greater than current question_id,
    # then get first question order by question_id ascend
    next_question = QuestionModel.query.filter(QuestionModel.id > current_question_id).order_by(
        QuestionModel.id.asc()).first()
    if next_question:
        return redirect(url_for('QUESTION.question_detail', question_id=next_question.id))
    else:
        # if there is no next_question, pop session and show result page to user
        flash('검사 완료', category="success")
        session.pop('user_id', None)
        answers = AnswerModel.query.filter_by(user_id=session_info['answered_user_id']).order_by(
            AnswerModel.id.asc()).all()
        return render_template('home/result.html', answered_user=session_info['answered_username'], answers=answers)


@question_blp.route('/detail/<int:question_id>/', methods=['GET', 'POST'])
def question_detail(question_id):
    # find question by question_id in QuestionModel
    question = QuestionModel.query.get_or_404(question_id)
    # use AnswerForm when POST requests
    # see forms/Answerform.py
    answer_form = AnswerForm(request.form)

    # container for session
    session_info = {}

    if request.method == 'POST' and answer_form.validate_on_submit():
        answer = get_from_data(answer_form)

        # get session info to verify current user is valid
        session_info = get_session_info()

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
                return get_next_question(question_id, session_info)
            except IntegrityError:
                db.session.rollback()
                flash('Integrity Error Occurs.', category="error")
            except Exception as e:
                db.session.rollback()
                flash(f"Error: {e}", category="error")
            return redirect(url_for('MAIN.index'))

    # if request.method == 'GET', just render question_detail page
    return render_template('question/question_detail.html', question=question, form=answer_form)
