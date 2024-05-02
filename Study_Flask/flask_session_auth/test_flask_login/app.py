from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask import Flask, render_template, session, redirect, url_for, flash

# https://flask-login.readthedocs.io/en/latest/#your-user-class
from models import User

from views import configure_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-secret-key'  # 세션관리를 위해 Secret key 설정

# https://flask-login.readthedocs.io/en/latest/#configuring-your-application
login_manager = LoginManager()  # flask_login 객체 사용
login_manager.init_app(app)
login_manager.login_view = 'login'  # login 화면이 띄워질 html 파일 명 설정


# https://flask-login.readthedocs.io/en/latest/#how-it-works
@login_manager.user_loader  # This callback is used to reload the user object from the user ID stored in the session
def load_user(user_id):
    return User.get(user_id)


configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
