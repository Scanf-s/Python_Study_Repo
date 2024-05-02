from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

# from datetime import timedelta
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 예: 7일

app.secret_key = 'your_secret_key'  # 실제 배포시에는 .env 파일에 따로 저장 필요
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # Session(cookie)의 유지기간을 7일로 설정

# 예시 사용자 데이터
users = {
    "john": "pw123",
    "leo": "pw123"
}


@app.route('/')
def index(): # 기본 접속시, login.html을 보여줌
    return render_template('login.html')


# 사용자가 login.html 폼을 통해 로그인 정보를 제출하면, login 뷰에서 이를 검증
# 검증이 성공하면, 사용자 이름을 세션에 저장하고 비밀 페이지로 리디렉션
@app.route('/login', methods=['POST']) # login post request
def login():
    username = request.form['username'] # request form 데이터에서 username을 가져옴
    password = request.form['password'] # request form 데이터에서 password를 가져옴
    if username in users and users[username] == password: # users 딕셔너리에 username과 password가 일치하는게 존재하면 성공
        session['username'] = username # 'username'세션 생성
        # session.permanent = True  # 세션 유지 기간을 활성화
        return redirect('/secret') # /secret 페이지로 redirect
    else: # 로그인 실패
        flash('Invalid username or password')
        return redirect('/')


# 인증된 사용자 페이지
# secret 뷰에서는 사용자가 로그인되어 있는지 세션을 통해 확인하고,
# 로그인되지 않은 사용자는 로그인 페이지로 리디렉션합니다.
@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')


# 사용자가 로그아웃 링크를 클릭하면,
# logout 뷰에서 세션에서 사용자 정보를 제거하고 초기 페이지로 리디렉션
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)