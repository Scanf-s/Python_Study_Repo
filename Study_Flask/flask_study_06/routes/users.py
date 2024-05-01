from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db

from models.models import User

users_blp = Blueprint('User', __name__, url_prefix='/users', description="Operations on users")


@users_blp.route('/', methods=['GET', 'POST'])
class UserList(MethodView):
    def get(self):
        users = User.query.all()  # select * from User
        return jsonify(
            [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "boards": [
                        {
                            "id": board.id,
                            "title": board.title,
                            "content": board.content
                        }
                        for board in user.boards.all()  # Execute the query and iterate over results
                    ]
                } for user in users
            ]
        )

    def post(self):
        data = request.json  # json 형태로 request를 받아온다.
        new_user = User(
            id=data['id'],
            name=data['name'],
            email=data['email']
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 200


@users_blp.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
class UserById(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)  # id = user_id 인것만 query 해오는 코드. 못가져오면 404
        return jsonify(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "boards": [
                    {
                        "id": board.id,
                        "title": board.title,
                        "content": board.content
                    }
                    for board in user.boards.all()
                ]
            }
        )

    def put(self, user_id):
        board = User.query.get_or_404(user_id)  # user_id에 해당하는 row를 가져온다.
        data = request.json  # 사용자의 request를 json으로 가져온다
        board.name = data['name']
        board.email = data['email']

        db.session.commit()
        return jsonify({"message": "User updated"}), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
