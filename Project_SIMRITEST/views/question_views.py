from flask import Blueprint, render_template, redirect, url_for
from models.model_definitions import QuestionModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


@question_blp.route('/', methods=['GET'])
def question_list():
    question_list = QuestionModel.query.order_by(QuestionModel.order_num.asc()).all()
    return render_template('question/question_list.html', question_list=question_list)


@question_blp.route('/detail/<int:question_id>/', methods=['GET'])
def question_detail(question_id):
    question = QuestionModel.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
