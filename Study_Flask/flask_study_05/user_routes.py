from flask_smorest import Blueprint, abort
from flask import request, jsonify


def create_user_blueprint(mysql):
    user_blp = Blueprint('user_routes', __name__, url_prefix='/users') # blueprint 생성

    @user_blp.route('/', methods=['GET']) # GET METHOD
    def get_users(): # 전체 데이터를 가져올 수 있는 메서드
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()  # fetchall()의 결과 값은 튜플 데이터
        cursor.close()

        # 튜플을 딕셔너리로 변환
        users_list = []
        for user in users:
            users_list.append({
                'id': user[0],
                'name': user[1],
                'email': user[2]
            })

        return jsonify(users_list)

    @user_blp.route('/', methods=['POST'])
    def add_user(): # POST METHOD
        user_data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                       (user_data['name'], user_data['email']))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User added successfully'}), 201

    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id): # PUT METHOD
        user_data = request.json

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s",
                       (user_data['name'], user_data['email'], user_id))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'User updated successfully'})

    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id): # DELETE METHOD
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'User deleted successfully'})

    return user_blp
