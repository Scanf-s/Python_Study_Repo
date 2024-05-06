from flask import Blueprint, render_template, flash, redirect, url_for
from flask import request

from app import db
from models.model_definitions import QuestionModel, AnswerModel

question_blp = Blueprint('QUESTION', __name__, url_prefix='/questions')


@question_blp.route('/', methods=['GET'])
def question_list():
    question_list = QuestionModel.query.order_by(QuestionModel.order_num.asc()).all()
    return render_template('question/question_list.html', question_list=question_list)


@question_blp.route('/detail/<int:question_id>/', methods=['GET', 'POST'])
def question_detail(question_id):
    question = QuestionModel.query.get_or_404(question_id)

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
            flash('Successfully added response', 'success')

            next_question = QuestionModel.query.get(question_id + 1)
            if next_question:
                return redirect(url_for('QUESTION.question_detail', question_id=next_question.id))
            else:
                flash('Question complete', 'success')
                # 추후 user_id와 해당 user_id의 최근 5개의 값을 가져오도록 수정할 예정임
                return render_template('home/result.html', answers=AnswerModel.query.order_by(AnswerModel.id.desc()).limit(5))

    return render_template('question/question_detail.html', question=question)
