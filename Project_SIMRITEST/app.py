from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate
from config.db import init_db, db
from views import main_views, question_views
from models.model_definitions import UserModel, AdminModel, AnswerModel, QuestionModel
from flask_login import LoginManager, login_user
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@127.0.0.1/simritest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cyborg'

init_db(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(main_views.main_blp)
app.register_blueprint(question_views.question_blp)

if __name__ == '__main__':
    app.run(debug=True)
