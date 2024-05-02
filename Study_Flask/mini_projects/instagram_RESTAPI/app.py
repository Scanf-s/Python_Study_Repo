from flask import Flask, render_template
from flask_smorest import Api
from instagram_RESTAPI.views.instagram import instagram_blp

app = Flask(__name__)

# API 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SECRET_KEY'] = "test_key"

# Blueprint 등록
api = Api(app)
api.register_blueprint(instagram_blp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)