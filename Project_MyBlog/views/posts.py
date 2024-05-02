from datetime import datetime

from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify, request

from config import database

from models.models import Post

post_blp = Blueprint('PostBluePrint', __name__, url_prefix='/posts', description="Operations on posts")


@post_blp.route('/', methods=['GET'])
class GetAllPosts(MethodView):
    def get(self):
        posts = Post.query.all()
        return jsonify(
            [
                {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "created_at": post.created_at
                } for post in posts
            ]
        ), 200


# 새로운 게시글 추가
@post_blp.route('/', methods=['POST'])
class AddNewPost(MethodView):
    def post(self):
        data = request.json  # json 형태로 request를 받아온다.
        new_board = Post(
            title=data['title'],
            content=data['content'],
            created_at=datetime.now()
        )

        database.session.add(new_board)
        database.session.commit()
        return jsonify({"message": "Created new post"}), 200


# Post ID로 특정 게시글 조회
@post_blp.route('/<int:post_id>', methods=['GET']) # 이와 같이 /<int:post_id> 같은 형태는 path parameter라고 한다.
class GetPostbyId(MethodView):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return jsonify(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at
            }
        )

# Post ID로 특정 게시글 수정
@post_blp.route('/<int:post_id>', methods=['PUT'])
class EditPostByID(MethodView):
    def put(self, post_id):
        post = Post.query.get_or_404(post_id)
        data = request.json  # json 형태로 request를 받아온다.

        post.title = data['title']
        post.content = data['content']
        database.session.commit()

        return jsonify({"message": "Updated post"}), 200


# Post ID로 특정 게시글 삭제
@post_blp.route('/<int:post_id>', methods=['DELETE'])
class DeletePostById(MethodView):
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        database.session.delete(post)
        database.session.commit()
        return jsonify({"message": "Deleted post"}), 200
