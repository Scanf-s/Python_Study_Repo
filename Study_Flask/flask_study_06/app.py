from flask import Flask, render_template
from flask_smorest import Api, abort
from db import db
from routes.board import board_blp
from routes.users import users_blp

app = Flask(__name__)
# https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)
api.register_blueprint(board_blp)
api.register_blueprint(users_blp)


@app.route("/manage-boards")
def manage_borads():
    return render_template('boards.html')


@app.route("/manage-users")
def manage_users():
    return render_template('users.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # SQLAlchemy로 연결된 mysql에, 내가 정의한 모든 database model (models.py) 생성
    app.run(debug=True)
