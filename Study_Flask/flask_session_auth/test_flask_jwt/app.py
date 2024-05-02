from flask import Flask, render_template
from views.user import user_blp
from jwt_utils import configure_jwt  # JWT 설정 함수를 임포트합니다.

app = Flask(__name__)
configure_jwt(app)  # JWT 관련 추가 설정을 적용합니다.

app.register_blueprint(user_blp, url_prefix='/user')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
