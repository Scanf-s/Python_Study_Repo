# Overview
이 프로젝트는, 간단한 심리테스트를 제공하는 Flask Application이다. 총 5문항으로 이루어져 있으며, Admin 기능을 통해 문항을 늘리거나 줄일 수 있다.

# Dependencies

## 1. Python 3.11
## 2. Flask 3.0.2
>Flask 공식 문서 : https://flask.palletsprojects.com/en/3.0.x/

백엔드 API 개발 및 웹 페이지 개발을 지원하는 웹 프레임워크이다.

## 3. Flask-SQLAlchemy 3.1.1
> SQLAlchemy 공식 문서 :
https://docs.sqlalchemy.org/en/20/
>
> Flask-SQLalchemy 공식 문서 :
https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/

Python 환경에서 ORM 기술을 통해 Database CRUD를 할 수 있도록 돕는 라이브러리이다.

## 4. Flask-Mysqldb
> Flaks-Mysqladb 공식 문서 :
https://pypi.org/project/Flask-MySQLdb/

Flask 프로젝트에 MySQL 데이터베이스 연결을 위해 사용하는 라이브러리이다.

## 5. Flask-Migrate
> Flask-Migrate 공식 문서 :
https://flask-migrate.readthedocs.io/en/latest/

SQLAlchemy의 확장 기능으로, DB 버전 관리 및 Flask Application이 실제 MySQL 데이터베이스 접근 및 제어 시 변경 사항을 반영할 수 있도록 돕는 라이브러리이다.

## 6. pandas, plotly
> Pandas 공식 문서:
> https://pandas.pydata.org/docs/
>
> Plotly 공식 문서:
https://plotly.com/python/

DB에 저장된 데이터를 시각화하여 보여주기 위해 사용하는 라이브러리이다.

# 프로젝트 구조
```yaml
\APP
│  database.py
│  models.py
│  routes.py
│  __init__.py
│
├─templates
│      admin.html
│      dashboard.html
│      index.html
│      manage_questions.html
│      quiz.html
│      quiz_list.html
│      results.html
│
└─__pycache__
        database.cpython-311.pyc
        database.cpython-312.pyc
        models.cpython-311.pyc
        models.cpython-312.pyc
        routes.cpython-311.pyc
        routes.cpython-312.pyc
        __init__.cpython-311.pyc
        __init__.cpython-312.pyc

```
## database.py
Flask sqlalchemy 사용을 위한 SQLAlchemy 인스턴스를 생성하는곳이다.
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

## models.py
SQLAlchemy를 통해 실제 database에 저장하기 위해 ORM Model을 선언한 파일이다.

```python
from datetime import datetime

from .database import db


class Participant(db.Model):
    __tablename__ = "participant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    order_num = db.Column(db.Integer, default=0)  
    is_active = db.Column(db.Boolean, default=True)


class Quiz(db.Model):
    __tablename__ = "quiz"
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey("participant.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    chosen_answer = db.Column(db.String(255))

    participant = db.relationship("Participant", backref="quizzes")
    question = db.relationship("Question", backref="quizzes")

```

### 1. Participant
이 객체는 테스트 응시자 정보를 db에 저장하기 위한 모델이다.

### 2. Admin
이 객체는 Admin 정보를 db에 저장하기 위한 모델이다.

### 3. Question
이 객체는 Question 정보를 db에 저장하기 위한 모델이다.

### 4. Quiz
이 객체는 Participant가 테스트에서 응답한 내용과 해당 Question 정보를 저장해서, 답변의 집합으로써 기능하는 모델이다.

## routes.py

``routes.py``는 flask Blueprint를 이용해 웹페이지의 route를 설정하고 관리하는 소스코드이다.

``routes.py``는 크게 데이터 시각화 함수와 라우팅 관리 함수로 나뉘며,
라우팅 함수에서는 admin route와 main route로 나뉜다.

### 1. main route

#### 127.0.0.1:5000/

```python
@main.route("/", methods=["GET"])
def home():
    # 참여자 정보 입력 페이지를 렌더링합니다.
    return render_template("index.html")
```

위 주소로 접근 (HTTP GET)시, templates 폴더의 index.html이 보여진다.


#### 127.0.0.1:5000/participants
```python
@main.route("/participants", methods=["POST"])
def add_participant():
    data = request.get_json()
    new_participant = Participant(
        name=data["name"], age=data["age"], gender=data["gender"] , created_at=datetime.utcnow()
    )
    db.session.add(new_participant)
    db.session.commit()

    # 리다이렉션 URL과 참여자 ID를 JSON 응답으로 전송
    return jsonify(
        {"redirect": url_for("main.quiz"), "participant_id": new_participant.id}
    )
```
이 함수는 사용자 정보를 받아오는 함수이다.
해당 route는 HTTP POST 요청시에만 실행되는 함수로, 위 주소에 POST 요청으로 아래와 같은 json 데이터가 들어오면,
```json
{
	name:"asdf"
  	age:"123"
  	gender:"asdf"
}
```
해당 json을 파이썬 코드로 처리하여 데이터베이스에 해당 사용자 정보를 저장하고, Response 메세지로 /participants에서 /quiz로 redirect하는 함수와 현재 저장한 User ID를 보낸다.

이렇게 return을 구성한 이유는, /participant 정보 입력 후, 바로 /quiz로 redirect 하여 질문 단계로 넘어가기 위함이며, 이와 함께 participant id를 넘긴 이유는 해당 사용자에 대한 응답을 기록해야하기 때문이다.

#### 127.0.0.1:5000/quiz
```python
@main.route("/quiz")
def quiz():
    # 퀴즈 페이지를 렌더링합니다. 참여자 ID 쿠키가 필요합니다.
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        # 참여자 ID가 없으면, 홈페이지로 리다이렉션합니다.
        return redirect(url_for("main.home"))

    questions = Question.query.all()
    questions_list = [question.content for question in questions]
    return render_template("quiz.html", questions=questions_list)
```

이 함수는, 퀴즈 페이지를 사용자에게 보여주기 위한 함수이다.

먼저, 해당 사용자의 세션을 조사하여, 유효한 사용자인지 조사한다.

쿠키가 존재한다면, `Question`데이터베이스에서 질문 데이터를 모두 가져온 뒤, Jinja로 구현된 quiz.html에 질문 데이터를 넘겨, 동적으로 페이지를 구현한다.

#### 127.0.0.1:5000/submit
```python
@main.route("/submit", methods=["POST"])
def submit():
    # 참여자 ID가 필요합니다.
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return jsonify({"error": "Participant ID not found"}), 400

    data = request.json
    quizzes = data.get("quizzes", [])

    for quiz in quizzes:
        question_id = quiz.get("question_id")
        chosen_answer = quiz.get("chosen_answer")

        # 새 Quiz 인스턴스 생성
        new_quiz_entry = Quiz(
            participant_id=participant_id,
            question_id=question_id,
            chosen_answer=chosen_answer,
        )
        # 데이터베이스에 추가
        db.session.add(new_quiz_entry)

    # 변경 사항 커밋
    db.session.commit()
    return jsonify(
        {
            "message": "Quiz answers submitted successfully.",
            "redirect": url_for("main.show_results"),
        }
    )
```

이 함수는 사용자가 설문(또는 퀴즈)항목 응답에 대해, 다음 또는 제출하기 버튼을 클릭하면, 해당 설문의 응답을 기록하는 submit()함수가 실행되어 사용자의 응답을 Database에 저장한다.

사용자의 응답은 templates/quiz.html의 sendResult() javascript 함수에서 json 형식으로 HTTP POST 요청을 보낸다. 해당 HTTP POST를 submit()함수에서 받아서, DB에 추가하는 방식이라고 생각하면 된다.

#### 127.0.0.1:5000/questions

```python
@main.route("/questions")
def get_questions():
    # is_active가 True인 질문만 선택하고, order_num에 따라 정렬
    questions = (
        Question.query.filter(Question.is_active == True)
        .order_by(Question.order_num)
        .all()
    )
    questions_list = [
        {
            "id": question.id,
            "content": question.content,
            "order_num": question.order_num,
        }
        for question in questions
    ]
    return jsonify(questions=questions_list)
```

해당 함수는, 사용자에게 보여줄 questions를 DB에서 꺼내와서 templates/quiz.html로 json 형태로 전달해주는 함수이다. 

해당 json data를 받는 부분은 quiz.html의 javascript 부분을 보면 알 수 있다.

```js
async function fetchQuestions() {
            const response = await fetch('/questions');
            const data = await response.json();
            return data.questions; // 수정됨: 질문 데이터 배열 반환
        }

        const questionElement = document.getElementById("question");
        const buttonsElement = document.getElementById("buttons");
        const resultPageElement = document.getElementById("resultPage");

        let currentQuestionIndex = 0;
        let userAnswers = [];
        let questions_list;

        async function initializeQuiz() {
            questions_list = await fetchQuestions();
            userAnswers = Array(questions_list.length).fill(null);
            showQuestion();
        }

        function showQuestion() {
            if (currentQuestionIndex < questions_list.length) {
                questionElement.innerText = questions_list[currentQuestionIndex].content;
                buttonsElement.style.display = "block";
                resultPageElement.style.display = "none";
            } else {
                questionElement.innerText = "심리테스트가 종료되었습니다.";
                buttonsElement.style.display = "none";
                resultPageElement.style.display = "block";
            }
        }
```

먼저 Javascript의 맨 아래부분을 보면, `initializeQuiz` 함수를 호출하는 것을 볼 수 있다.

`initializeQuiz` 함수 내부에서 또 `fetchQuestion()`을 호출하는데 해당 함수가 바로 quiz json data를 받아오는 곳이다.

따라서, 해당 함수에서 json을 parse하여 list 형태로 변환 후, 다시 `initializeQuiz`로 넘겨주면, `showQuestion()`을 통해 **동적으로 퀴즈 페이지를** 보여주게 된다.
  
#### 127.0.0.1:5000/results

해당 부분은 사용자가 응답한 결과를 보여주는 부분이다.

Pandas와 Ploty를 사용하여 시각화 하는 부분에 대해서는 코드가 길고, 필자가 Pandas, ploty를 사용해본적이 없어서 넘어가도록 하겠다.

### 2. admin route

admin blueprint 설정으로, url_prefix="/admin/이 있는데, 이는 해당 blueprint를 사용하는 요청은 무조건 /admin을 끼고 시작한다고 생각하면 된다.

즉, @admin.route("", method=['GET'])은
`127.0.0.1:5000/`으로 접근하는것이 아니라, `127.0.0.1:5000/admin`으로 접근하는 것이다.

#### 127.0.0.1:5000/admin
```python
@admin.route("", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password, password):
            session["admin_logged_in"] = True
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Invalid username or password")

    return render_template("admin.html")
```
해당 함수는 admin/dashboard로 redirect 하기 전, admin login을 하도록 요구하는 함수이다.

#### 127.0.0.1:5000/admin/logout
```python
@admin.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin.login"))
```
어드민 페이지에서 logout HTTP GET Request를 보내면, 해당 함수가 실행되어 session 정보를 삭제하고, 다시 /admin으로 redirect해버리는 함수이다.


#### 127.0.0.1:5000/admin/dashboard
```python
@admin.route("dashboard")
@login_required
def dashboard():
    # 날짜별 참가자 수를 계산
    participant_counts = (
        db.session.query(
            func.date(Participant.created_at).label("date"),
            func.count(Participant.id).label("count"),
        )
        .group_by("date")
        .all()
    )

    # 날짜와 참가자 수를 분리하여 리스트에 저장
    dates = [result.date for result in participant_counts]
    counts = [result.count for result in participant_counts]

    # Plotly 그래프 생성
    graph = go.Figure(go.Scatter(x=dates, y=counts, mode="lines+markers"))

    graph.update_layout(title="일자별 참가자 수", xaxis_title="날짜", yaxis_title="참가자 수")

    # Plotly 그래프를 HTML로 변환
    graph_div = plot(graph, output_type="div", include_plotlyjs=False,config = {'displayModeBar': False})

    # 생성된 HTML을 템플릿으로 전달
    return render_template("dashboard.html", graph_div=graph_div)
```
해당 함수를 통해 admin dashboard를 보려면 먼저 admin login을 해야 한다. `@login_required`

Database에서 필요한 정보를 query해온 뒤, 시각화 하여 Admin user에게 해당 정보를 보여주는 함수이다.



#### 127.0.0.1:5000/admin/dashboard/question
```python
@admin.route("/dashboard/question", methods=["GET", "POST"])
@login_required
def manage_questions():
    if request.method == "POST":
        if "new_question" in request.form:
            # 새 질문 추가
            is_active = (
                "is_active" in request.form and request.form["is_active"] == "on"
            )
            new_question = Question(
                content=request.form["content"],
                order_num=request.form["order_num"],
                is_active=is_active,
            )
            db.session.add(new_question)
            db.session.commit()
        else:
            # 기존 질문 수정
            question_id = request.form["question_id"]
            question = Question.query.get(question_id)
            if question:
                is_active = (
                    "is_active" in request.form and request.form["is_active"] == "on"
                )
                question.content = request.form["content"]
                question.order_num = request.form["order_num"]
                question.is_active = is_active
                db.session.commit()

    questions = Question.query.order_by(Question.order_num).all()
    return render_template("manage_questions.html", questions=questions)
```
해당 함수는 Database에 설문 항목을 추가해주는 함수이다. 

원하는 내용을 `templates/manage_questions.html`에 입력하여 Form 형식으로 HTTP POST 요청을 보내면, Database에 저장하는 기능이 있으며,

기존 질문 내용을 수정하는 기능도 존재한다.

#### 127.0.0.1:5000/admin/dashboard/list
```python
@admin.route("/dashboard/list")
@login_required
def quiz_list():
    quizzes = Quiz.query.all()
    return render_template("quiz_list.html", quizzes=quizzes)
```

현재 Quiz list를 보여주는 함수이다.

##
