from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]


@app.route('/')
def index():
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)