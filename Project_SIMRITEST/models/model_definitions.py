import enum
from datetime import datetime
from flask_login import UserMixin
from config.db import db


class AgeEnum(enum.Enum):
    tens = "10"
    twenties = "20"
    thirties = "30"
    fourties = "40"
    fifties = "50"


class GenderEnum(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    age = db.Column(db.Enum(AgeEnum), nullable=False)
    gender = db.Column(db.Enum(GenderEnum), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)


# inherit UserMixin, we can have is_authenticated, is_active, is_anonymous, get_id functions
# these methods are required when we manage user auth status and sessions
class AdminModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)


class QuestionModel(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255))
    order_num = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)


class AnswerModel(db.Model):
    # ON DELETE CASCADE
    # https://docs.sqlalchemy.org/en/20/orm/cascades.html#using-foreign-key-on-delete-cascade-with-orm-relationships
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id", ondelete='CASCADE'))
    question = db.relationship('QuestionModel', backref=db.backref('answer_set'))
    chosen_answer = db.Column(db.String(255))
