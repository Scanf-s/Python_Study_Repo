from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask import request

from app import db
from models.model_definitions import QuestionModel, AnswerModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


@question_blp.route('/', methods=['GET'])
def question_list():
    session_user_id = session.get('user_id', None)
    if session_user_id:
        # only user has session id can response questions
        question_list = QuestionModel.query.order_by(QuestionModel.order_num.asc()).all()
        return render_template('question/../templates/admin/question_list.html', question_list=question_list)
    else:
        # if user has no session info, redirect to main.index
        return redirect(url_for('MAIN.index'))

@question_blp.route('/detail/<int:question_id>/', methods=['GET', 'POST'])
def question_detail(question_id):
    # find question by question_id in QuestionModel
    question = QuestionModel.query.get_or_404(question_id)

    if request.method == 'POST':
        # in question_detail.html, if user sends form called 'response(yes or no radio button)'
        user_response = request.form.get('response')
        if user_response:
            answered_user_id = session.get('user_id', None)
            answered_username = session.get('username', None)
            # if current user has session(cookie)
            if answered_user_id and answered_username:
                # make model to insert mysql database
                response = AnswerModel(
                    user_id=answered_user_id,
                    question_id=question_id,
                    chosen_answer=user_response
                )
                db.session.add(response)
                db.session.commit()
                flash('Successfully added response', 'success')

            # filter only questions that greater than current question_id,
            # then get first question order by question_id ascend
            next_question = QuestionModel.query.filter(QuestionModel.id > question_id).order_by(QuestionModel.id.asc()).first()
            if next_question:
                return redirect(url_for('QUESTION.question_detail', question_id=next_question.id))
            else:
                # if there is no next_question, pop session and show result page to user
                flash('Question complete', 'success')
                session.pop('user_id', None)
                answers = AnswerModel.query.filter_by(user_id=answered_user_id).order_by(AnswerModel.id.desc()).all()
                return render_template('home/result.html', answered_user=answered_username, answers=answers)

    # if request.method == 'GET', just render question_detail page
    return render_template('question/question_detail.html', question=question)
