from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Cascade로 인해, 질문을 삭제하면 답변도 같이 삭제됨
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # Answer 모델에서 Question 모델을 참조하기 위해 사용한다
    # 이렇게 참조하면, answer.question.subject를 통해 Answer에서 Question의 속성을 참조할 수 있다.
    # 첫번째 인자 : 참조할 모델명
    # 두번째 인자 : 역참조 설정 (해당 질문에 달린 여러개의 답변들을 참조할 수 있도록 설정)
    # 즉, 질문 객체 quest1이 있을 때, quest1.answer_set을 이용하여 참조할 수 있다.
    # cascade='all, delete-orphan'을 통해 질문 객체에서 삭제 함수를 호출할 때, 딸린 답변들도 모두 삭제 가능하다.
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
