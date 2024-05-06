from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

main_blp = Blueprint('MAIN', __name__, url_prefix='/')


@main_blp.route('/')
def hello():
    return redirect(url_for('MAIN.index'))


@main_blp.route('/hello')
def index():
    return render_template('home/index.html')


@main_blp.route('/result')
def result():
    return render_template('home/result.html')
