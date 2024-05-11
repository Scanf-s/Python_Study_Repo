from flask import request, redirect, url_for, jsonify
from flask_smorest import Blueprint
from user_management_project.models.data import users
from flask import flash, render_template

manage_blp = Blueprint('manage_blp', __name__, template_folder='templates')


@manage_blp.route('/', methods=['GET'])
def show_user():
    return render_template('index.html', users=users)


@manage_blp.route('/', methods=['POST'])
def add_user():
    if 'username' not in request.form or 'nickname' not in request.form:
        # request에 둘중 하나가 빠져있다면 error 메세지 생성 후, redirect
        flash('Missing username or nickname', 'error')
        return redirect(url_for('manage_blp.show_user'))

    username = request.form['username']
    nickname = request.form['nickname']

    # Check if the username already exists
    if any(user['username'] == username for user in users):
        flash('Username already exists', 'error')
        return redirect(url_for('manage_blp.show_user'))  # 에러메세지 출력 후에, index.html로 redirect

    # Add new user if not existing
    users.append({'username': username, 'nickname': nickname})
    flash('User added successfully', 'success')
    return redirect(url_for('manage_blp.show_user'))  # 성공했다면 index.html로 redirect


@manage_blp.route('/update', methods=['PUT'])
def update_username():
    # json으로 PUT HTTP를 받아옴
    data = request.get_json()
    if not data or 'username' not in data or 'nickname' not in data:
        flash('Missing username or nickname', 'error')
        return jsonify({'error': 'Missing username or nickname'}), 400

    username = data['username']
    nickname = data['nickname']

    # users에 user가 있는지 확인
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('Username does not exist', 'error')
        return jsonify({'error': 'Username does not exist'}), 404

    # 닉네임 변경
    user['nickname'] = nickname
    flash('User updated successfully', 'success')
    return jsonify({'message': 'User updated successfully'}), 200


@manage_blp.route('/delete', methods=['DELETE'])
def delete_user_by_username():
    username = request.get_json()['username']
    if username is None:
        flash('Json username not found', 'error')
        return jsonify({'error': 'Json username not found'}), 404

    # users에 user가 있는지 확인
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('Username does not exist', 'error')
        return jsonify({'error': 'Username does not exist'}), 404

    users.remove(user)
    flash('User deleted successfully', 'success')
    return jsonify({'message': 'User deleted successfully'}), 200

