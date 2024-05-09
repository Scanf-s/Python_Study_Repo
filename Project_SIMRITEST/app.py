from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from config.db import init_db, db
from config.app_config import (
    SECRET_KEY,
    DATABASE,
    USERNAME,
    PASSWORD,
    ADDRESS,
    PORT,
    DATABASE_NAME
)
from models.model_definitions import AdminModel
from views import main_views, question_views, admin_views

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'{DATABASE}://{USERNAME}:{PASSWORD}@{ADDRESS}:{PORT}/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
migrate = Migrate(app, db)


# Register blueprints
app.register_blueprint(main_views.main_blp)
app.register_blueprint(question_views.question_blp)
app.register_blueprint(admin_views.admin_blp)


# Initialize Flask-Login lib
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin.login'

# Initialize Flask-WTF lib
csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return AdminModel.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
