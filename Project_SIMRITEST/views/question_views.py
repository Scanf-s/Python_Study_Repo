from flask import request
from app import db
from flask import Blueprint, render_template, redirect, url_for
from models.model_definitions import QuestionModel, AnswerModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


@question_blp.route('/', methods=['GET'])
def question_list():
    question_list = QuestionModel.query.order_by(QuestionModel.order_num.asc()).all()
    return render_template('question/question_list.html', question_list=question_list)


@question_blp.route('/detail/<int:question_id>/', methods=['GET', 'POST'])
def question_detail(question_id):
    if request.method == 'POST':
        user_response = request.form.get('response')
        if user_response:
            response = AnswerModel(
                user_id=1,
                question_id=question_id,
                chosen_answer=user_response
            )
            db.session.add(response)
            db.session.commit()
            return redirect(url_for('QUESTION.question_list'))

    question = QuestionModel.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
