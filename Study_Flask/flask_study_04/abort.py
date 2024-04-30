from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the request.")

    # 정상적인 응답
    return "Success!"