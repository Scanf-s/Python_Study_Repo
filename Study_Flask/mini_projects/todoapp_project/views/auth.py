from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from todoapp_project.models.models import User
from werkzeug.security import check_password_hash

auth_blp = Blueprint('auth', 'auth',
                     url_prefix='/login', description='Operations on todos')


@auth_blp.route('/', methods=['POST'])
def login():
    if not request.is_json:
        print('if not request.is_json')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        print('if not username or not password')
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    print('user 여기는오나', user)
    print('user 여기는오나', check_password_hash(user.password_hash, password))
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username)
        print('access_token', access_token)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401
