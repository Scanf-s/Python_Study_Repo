from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate
from config.db import init_db, db
from views import main_views, question_views
from models.model_definitions import UserModel, AdminModel, AnswerModel, QuestionModel
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from datetime import datetime

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


@login_manager.user_loader
def load_user(user_id):
    return AdminModel.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register():
    # If the user made a POST request, create a new user
    if request.method == "POST":
        user = AdminModel(
            username=request.form.get("username"),
            password=request.form.get("password"),
            is_admin=True,
            created_at=datetime.now()
        )
        db.session.add(user)
        db.session.commit()

        # Once user account created, redirect them
        # to login route
        return redirect(url_for("login"))
    # Renders sign_up template if user made a GET request
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = AdminModel.query.filter_by(username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        if user.password == request.form.get("password"):
            # Use the login_user method to log in the user
            login_user(user)
            return redirect(url_for("home"))
        # Redirect the user back to the home
        # (we'll create the home route in a moment)
    return render_template("login.html")


@app.route("/")
def home():
    # Render home.html on "/" route
    return render_template("home.html")



# Register blueprints
app.register_blueprint(main_views.main_blp)
app.register_blueprint(question_views.question_blp)

if __name__ == '__main__':
    app.run(debug=True)
