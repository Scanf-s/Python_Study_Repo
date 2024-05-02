from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import User, users


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.get(username)
            if user and users[username]['password'] == password:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password')
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/protected')
    @login_required
    def protected():
        return '<h1>Protected area</h1> <a href="/logout">Logout</a>'
