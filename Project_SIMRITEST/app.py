from flask import Flask, redirect, url_for, request, render_template
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from wtforms import form, validators
from wtforms.fields.simple import StringField
from flask_login import LoginManager, current_user, login_user, logout_user

from flask_admin import AdminIndexView, helpers, expose, Admin
from flask_admin.contrib.sqla import ModelView

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Temporary secret key for project
app.config['SECRET_KEY'] = 'secret'

# config database using mysql + sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/simritest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# define user model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    # flask-login integration
    # More details : https://flask-login.readthedocs.io/en/latest/#your-user-class
    # Referenced : https://github.com/flask-admin/flask-admin/blob/7fa26ab227868ff7512bb25c26a30fd7d69184bc/examples/auth-flask-login/app.py

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.login_id


# To use flask-login lib, define login and registration form
class LoginForm(form.Form):
    # Reason of using validators.input_required() : https://wtforms.readthedocs.io/en/3.1.x/validators/?highlight=required#wtforms.validators.InputRequired
    login_id = StringField('login_id', validators=[validators.input_required()])
    password = StringField('password', validators=[validators.input_required()])

    def validate_login(self):
        user = self.get_user()

        if user is None:
            # ValidationError : https://wtforms.readthedocs.io/en/3.1.x/validators/?highlight=validationerror#wtforms.validators.ValidationError
            raise validators.ValidationError('Invalid login')

    def get_user(self):
        return db.session.query(UserModel).filter_by(login_id=self.login_id).first()


# Initialize flask-login
def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    # user loader function
    @login_manager.user_loader
    def user_loader(login_id):
        # user_loader : https://flask-login.readthedocs.io/en/latest/#how-it-works
        return db.session.query(UserModel).filter_by(login_id=login_id).first()


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# Customize flask-admin: AdminIndexView
class MyAdminIndexView(AdminIndexView):

    # flask-admin : @expose https://flask-admin.readthedocs.io/en/latest/api/mod_base/
    # It is responsible for exposing a particular class method(index, login_view, logout_view) to a route on a web page
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:  # if current user is not authenticated (not logged in status)
            return redirect(url_for('.login_view'))  # redirect to below login_view function (/login)
        return super(MyAdminIndexView, self).index()

    @expose('/login', methods=['GET', 'POST'])
    def login_view(self):
        form = LoginForm(request.form)
        # flask-admin validate_form_on_submit : https://flask-admin.readthedocs.io/en/latest/api/mod_helpers/
        if helpers.validate_form_on_submit(form):
            user = form.get_user()  # get user from form data
            login_user(user)  # use flask-login login_user function to log in

        if current_user.is_authenticated:
            return redirect(url_for('.index'))

        return super(MyAdminIndexView, self).index()

    @expose('/logout')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask_login
init_login()

# create admin
admin = Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html')

if __name__ == "__main__":
    test_user = UserModel(
        login_id='admin',
        password=generate_password_hash('test123')
    )
    db.session.add(test_user)
    db.session.commit()
    app.run(debug=True)
