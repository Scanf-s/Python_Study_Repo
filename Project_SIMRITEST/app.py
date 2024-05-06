from flask import Flask
from flask_migrate import Migrate
from config.db import init_db, db
from views import main_views, question_views
from models.model_definitions import UserModel, AdminModel, AnswerModel, QuestionModel
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@127.0.0.1/simritest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cyborg'

init_db(app)
migrate = Migrate(app, db)

# Initialize Flask-Admin lib

# Initialize Flask-Login lib
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin.login'


# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return AdminModel.query.get(int(user_id))


# Register blueprints
app.register_blueprint(main_views.main_blp)
app.register_blueprint(question_views.question_blp)

if __name__ == '__main__':
    app.run(debug=True)
