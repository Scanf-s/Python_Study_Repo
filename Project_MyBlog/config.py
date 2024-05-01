# 데이터베이스 설정 파일
from flask_sqlalchemy import SQLAlchemy


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@localhost/blog'
SQLALCHEMY_TRACK_MODIFICATIONS = False

database = SQLAlchemy()
