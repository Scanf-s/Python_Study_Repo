from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from todoapp_project.db import db
from flask_migrate import Migrate

from todoapp_project.views.auth import auth_blp
from todoapp_project.views.todo import todo_blp


app = Flask(__name__)

# 데이터베이스 및 JWT 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# API에 Blueprint 등록
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)