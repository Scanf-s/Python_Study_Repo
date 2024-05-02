from flask import Flask, render_template, session, redirect, make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()  # HTTP인증을 사용하기 위해 객체 생성

# 사용자 정보
users = {
    "admin": "secret",
    "guest": "guest"
}


@auth.verify_password  # PW 검증 함수
def verify_password(username, password):
    """
    사용자 이름과 비밀번호가 유효한지 확인하는 함수를 정의합니다.
    간단한 사전 users를 사용하여 사용자 이름과 비밀번호를 확인합니다.
    실전 환경에서는 데이터베이스 또는 다른 안전한 저장소를 사용해야합니다.
    """
    if username in users and users[username] == password:
        return username


@app.route('/protected')
@auth.login_required  # 인증된 사용자만 해당 라우트로 접근할 수 있도록하는 목적. 사용자 인증을 요구.
def protected():
    return render_template('secret.html')


@app.route('/logout')
def logout():
    """401 Unauthorized 응답을 보내서 인증 초기화"""
    return make_response(
        '로그인 세션이 종료되었습니다. 다시 로그인 해주세요.',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


@app.route('/')
def index():  # 기본 접속시, login.html을 보여줌
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
