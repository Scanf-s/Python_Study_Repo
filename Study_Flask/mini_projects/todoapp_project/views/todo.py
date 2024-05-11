from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from todoapp_project.models.models import Todo, User
from todoapp_project.db import db

todo_blp = Blueprint('todo', 'todo', url_prefix='/todo', description='Operations on todos')


@todo_blp.route('/', methods=['POST'])
@jwt_required()
def create_todo():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    title = request.json.get('title', None)
    if not title:
        return jsonify({"msg": "Missing title"}), 400

    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()

    new_todo = Todo(title=title, user_id=user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"msg": "Todo created", "id": new_todo.id}), 201

# Todo 조회 (GET)
@todo_blp.route('/', methods=['GET'])
@jwt_required()
def get_todos():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    todos = Todo.query.filter_by(user_id=user.id).all()
    return jsonify([{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos])

# Todo 수정 (PUT)
@todo_blp.route('/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if 'title' in request.json:
        todo.title = request.json['title']
    if 'completed' in request.json:
        todo.completed = request.json['completed']
    db.session.commit()
    return jsonify({"msg": "Todo updated", "id": todo.id})

# Todo 삭제 (DELETE)
@todo_blp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "Todo deleted", "id": todo_id})