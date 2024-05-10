from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask import request

from forms.Answerform import AnswerForm
from models.model_definitions import AnswerModel
from views.question_util.utils import (
    get_session_info,
    verify_question_order_num,
    insert_answer_in_database,
    get_form_data,
    redirect_next_question
)

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


@question_blp.route('/result', methods=['GET'])
def question_result():
    session_info = get_session_info()
    flash('검사 완료', category="success")
    session.pop('user_id', None)
    answers = AnswerModel.query.filter_by(user_id=session_info['answered_user_id']).order_by(
        AnswerModel.id.asc()).all()
    return render_template(
        'question/result.html',
        answered_user=session_info['answered_username'],
        answers=answers
    )


@question_blp.route('/detail/<int:question_order_num>/', methods=['GET', 'POST'])
def question_detail(question_order_num):
    # get session info to verify the current user is valid
    session_info = get_session_info()
    # if there is no session info, redirect to user_info page
    if not session_info['answered_username']:
        flash("Please enter your information", category="warning")
        return redirect(url_for('MAIN.user_info'))

    # get question if question order number less than 5
    question = verify_question_order_num(question_order_num)

    # Answer form
    answer_form = AnswerForm(request.form)
    if request.method == 'POST' and answer_form.validate_on_submit():
        if insert_answer_in_database(get_form_data(answer_form), session_info, question.id):
            return redirect_next_question(question_order_num, session_info)

    # if request.method == 'GET', just render question_detail page
    return render_template(
        'question/question_detail.html',
        question_order_num=question_order_num,
        question=question,
        form=answer_form
    )
