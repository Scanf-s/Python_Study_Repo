from flask import redirect, jsonify, request, url_for, flash
from flask_smorest import Blueprint
from flask.views import MethodView
from instagram_RESTAPI.models.data import users

instagram_blp = Blueprint('instagram_blp', __name__, url_prefix='/users', template_folder='templates')


@instagram_blp.route('/', methods=['GET'])
@instagram_blp.response(200)
def get():
    """Retrieve all users and their posts."""
    return jsonify(
        [
            {
                "username": user['username'],
                "posts": [
                    {
                        "title": post['title'],
                        "likes": post['likes']
                    } for post in user['posts']
                ]
            } for user in users
        ]
    )


@instagram_blp.route('/', methods=['POST'])
@instagram_blp.response(201)
def post():
    data = request.get_json()
    user = next((user for user in users if user['username'] == data['username']), None)
    if user:
        flash('Username already taken')
        return redirect(url_for('instagram_blp.get'))

    new_user = {
        "username": data['username'],
        "posts": []
    }

    users.append(new_user)
    return jsonify(new_user)


@instagram_blp.route('/post/<string:username>', methods=['POST'])
def add_temp_post_by_username(username):
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('User not found')
        return redirect(url_for('instagram_blp.get'))

    user['posts'].append({"title": "temp_title", "likes": 0})
    return jsonify('Successfully added post')


@instagram_blp.route('/post/<string:username>', methods=['GET'])
def get_post_by_username(username):
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('User not found')
        return redirect(url_for('instagram_blp.get'))

    return jsonify(user['posts'])


@instagram_blp.route('/post/like/<string:username>/<string:title>', methods=['PUT'])
def like_post_by_username_and_title(username, title):
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('User not found')
        return redirect(url_for('instagram_blp.get'))

    post = next((post for post in user['posts'] if post['title'] == title), None)
    if not post:
        flash('Post not found')
        return redirect(url_for('instagram_blp.get'))

    post['likes'] += 1
    return jsonify(post)


@instagram_blp.route('/<string:username>', methods=['DELETE'])
def delete_user_by_username(username):
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        flash('User not found')
        return redirect(url_for('instagram_blp.get'))

    users.remove(user)
    return jsonify('Successfully deleted user')
