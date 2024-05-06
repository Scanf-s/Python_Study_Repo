from flask import Blueprint, url_for
from werkzeug.utils import redirect

main_blp = Blueprint('MAIN', __name__, url_prefix='/')


@main_blp.route('/hello')
def hello_pybo():
    return 'SIMRITEST HELLO PAGE'


@main_blp.route('/')
def index():
    return redirect(url_for('QUESTION.question_list'))  # Using blueprint 'QUESTION', route to 'question_list'
