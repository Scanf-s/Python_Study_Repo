from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask_jwt_extended import get_jwt

from test_flask_jwt.models.user import User
from test_flask_jwt.blocklist import add_to_blocklist

user_blp = Blueprint('user', __name__)

# 임시 사용자 데이터
users = {
    'user1': User('1', 'user1', 'pw123'),
    'user2': User('2', 'user2', 'pw123')
}


@user_blp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = users.get(username)
        if user and user.password == password:
            access_token = create_access_token(identity=username)  # jwt  생성
            refresh_token = create_refresh_token(identity=username)  # jwt 갱신
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    else:
        return render_template('login.html')


@user_blp.route('/protected', methods=['GET'])
@jwt_required()  # jwt가 존재하는 user만 protected page에 접근 가능
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@user_blp.route('/protected_page')
def protected_page():
    return render_template('protected.html')


@user_blp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    add_to_blocklist(jti)  # jti를 블랙리스트에 추가
    return jsonify({"msg": "Successfully logged out"}), 200
