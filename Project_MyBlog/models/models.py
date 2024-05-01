# database table model 정의
from config import database


class Post(database.Model):
    __tablename__ = 'posts'

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.String(100), nullable=False)
    content = database.Column(database.Text)
    created_at = database.Column(database.DateTime, nullable=False)
