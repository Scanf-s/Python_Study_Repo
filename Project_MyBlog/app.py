# 서버 시작 파일
# How to use mysql in flask?
# https://stackoverflow.com/questions/9845102/using-mysql-in-flask
from flask import Flask, render_template
from flask_smorest import Api
from flask_migrate import Migrate

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, database

from views.posts import post_blp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
database.init_app(app)
migrate = Migrate(app, database)
# migrate를 통해 database 'blog'에
# 내가 models에 정의한 Post 테이블을 실제 MySQL에 저장 가능하다.
# flask run 이전에, 다음 명령어를 통해 수행할 수 있다.
# 1. flask db init -> migration 환경 초기화
# 2. flask db migrate -> migration 파일 생성 -> 실제 프로젝트 폴더에 migrations 파일이 생성된다.
# 3. flask db upgrade -> 실제 DB에 Migration 적용 -> MySQL에서 확인

# blueprint 설정 및 등록
app.config["API_TITLE"] = "Blog API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)
api.register_blueprint(post_blp)

@app.route("/posts")
def main_posts():
    return render_template('posts.html')
