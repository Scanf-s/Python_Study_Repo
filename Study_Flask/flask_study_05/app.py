from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
# user_routes에서 Blueprint 직접 임포트 대신 함수 임포트
from user_routes import create_user_blueprint

app = Flask(__name__)

# MySQL 연결 설정
app.config['MYSQL_HOST'] = 'localhost' # 연결 주소
app.config['MYSQL_USER'] = 'root' # ID
app.config['MYSQL_PASSWORD'] = '123123' # PW
app.config['MYSQL_DB'] = 'oz' # DB name

mysql = MySQL(app)

# blueprint 생성 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

user_blp = create_user_blueprint(mysql)
api = Api(app)
api.register_blueprint(user_blp)


from flask import render_template
@app.route('/users_interface') # 경로 설정
def users_interface():
    return render_template('users.html') # 자동으로 templates 폴더 안에있는 users.html 파일을 찾는다