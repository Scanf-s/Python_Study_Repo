from db import db


# 사용자 테이블
# SQLAlchemy의 db.Model을 상속받아 테이블을 구현한다.
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    """
    User 모델의 boards 필드: 사용자가 작성한 모든 게시물(Board)들의 목록을 나타냅니다. 
    backref='author'는 Board 모델의 author 필드와 이 관계를 양방향으로 연결합니다.
    """
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')


# 게시글 테이블
class Board(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    author = db.relationship('User', back_populates='boards')


"""
User 모델의 boards 필드는 User와 Board 간의 관계를 정의합니다. 
이 필드를 통해 특정 사용자가 작성한 모든 게시글을 쉽게 접근할 수 있습니다. 
back_populates 옵션은 Board 모델의 author 필드와 이 관계를 양방향으로 연결합니다. 
lazy='dynamic' 옵션은 이 관계에 대한 쿼리가 실행될 때까지 로드를 지연시킵니다. 이는 대규모 데이터셋에서 성능을 최적화할 때 유용합니다.

Board 모델의 author 필드는 User 모델과의 관계를 설정하고, User의 boards 필드와 상호 작용합니다. 이 필드를 통해 특정 게시글의 작성자 정보에 접근할 수 있습니다.
"""