from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'title': 'Flask Jinja Template',
        'user': 'sullung',
        'is_admin': True,
        'Items': ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    }

    # (1) rendering 할 html 파일명 입력
    # (2) html로 넘길 데이터 입력
    return render_template('index.html', data=data)


"""
GET METHODS
"""


@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():  # 전체 게시글 조회
    # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
    return {
        'result': 'success',
        'data': {"feed1": "data", "feed2": "data2"}
    }


@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    return jsonify(
        {'result': 'success',
         'feed_id': feed_id,
         'data': {"feed1": "data"}
         }
    )


"""
POST METHODS
"""


@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result': 'success'})


# 또다른 예제
datas = [{"name": "item1", "price": 10}]


@app.route("/ap1/v1/datas", methods=['GET'])
def get_datas():
    return {'datas': datas}


@app.route("/api/v1/datas", methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {'name': request_data.get("name"), 'price': request_data.get("price")}
    datas.append(new_data)
    print(datas)
    return new_data, 201
