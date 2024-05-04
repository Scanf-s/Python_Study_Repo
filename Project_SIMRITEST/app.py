from flask import Flask, render_template, request, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'temp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12341234@localhost/simritest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import db
from sqlalchemy import Integer, String


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    email = db.Column(String(200), nullable=False, unique=True)
    password = db.Column(String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin  # `is_admin`은 admin 여부를 확인하는 속성


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


@app.route('/')
def index():
    return render_template('index.html')


# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.password == request.form['password']:  # 여기서는 해싱된 패스워드 비교로 변경해야 함
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')


admin = Admin(app, name='admin', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
