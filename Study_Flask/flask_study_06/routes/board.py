from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db

from models.models import Board

board_blp = Blueprint('Board', __name__, url_prefix='/board', description="Operations on boards")
# Board : blueprint 이름
# __name__ : import 시 사용하는 이름 (파일명이므로 board로 import)
# url_prefix : 브라우저에서 해당 경로를 통해 이동 가능

# API List
"""
Flask에서 MethodView를 사용하는 주요 이유는 클래스 기반 뷰를 생성하여 각 HTTP 메소드에 대한 핸들러를 메소드로 구분할 수 있게 해주기 때문입니다. 
이 접근 방식은 각각의 HTTP 메소드에 대한 로직을 명확하게 분리할 수 있어 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

1. 코드 조직화와 가독성 향상: Flask의 MethodView를 사용하면 GET, POST, PUT, DELETE 같은 다양한 HTTP 메소드를 클래스 내부의 별도 메소드로 정의할 수 있습니다. 
이 방식은 각 HTTP 메소드에 대한 처리 로직을 명확하게 구분하고, 뷰 로직이 특정 HTTP 메소드에 매핑되는 것을 쉽게 이해할 수 있도록 합니다.

2. 재사용성과 확장성: MethodView 기반의 클래스를 사용하면 공통 기능을 메소드로 쉽게 추출하고 상속을 통해 확장할 수 있습니다. 
예를 들어, 여러 뷰에서 공통으로 사용하는 인증 검사, 요청 데이터 검증, 로깅 등의 기능을 부모 클래스에 구현하고 이를 상속받아 사용할 수 있습니다.

3. 유연한 URL 라우팅 처리: MethodView를 사용하면 뷰를 add_url_rule 함수를 사용하여 프로그래밍적으로 URL에 연결할 수 있습니다. 
이는 동적으로 URL 룰을 생성하거나 애플리케이션의 다른 부분에서 뷰를 재사용하는 경우 유용합니다.

4. 보다 명시적인 뷰 <-> 경로 매핑: Flask의 전통적인 뷰 함수 방식 대신 MethodView를 사용하면 뷰의 클래스 이름과 HTTP 메소드 처리 로직이 명확하게 연결되므로 더 명시적인 매핑이 가능해집니다. 
이는 큰 프로젝트에서 뷰의 역할을 파악하기 쉽게 해줍니다.

5. 좋은 프레임워크 통합: 많은 Flask 확장 기능이 MethodView와 잘 통합되어 있습니다. 
예를 들어, Flask-RESTful 같은 확장은 REST API를 구축할 때 MethodView를 활용하여 각 리소스를 클래스로 표현하고, HTTP 메소드에 따라 적절히 요청을 처리하도록 설계되어 있습니다.
"""

# /board/
# 전체 게시글 가져오는 API (GET)
# 게시글 작성 (POST)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all() # select * from Board
        return jsonify([{"user_id": board.user_id,
                         "title": board.title,
                         "id": board.id,
                         "content": board.content,
                         "author": board.author.name
                         } for board in boards]
                       )

    def post(self):
        data = request.json # json 형태로 request를 받아온다.
        new_board = Board(
            title=data['title'],
            content=data['content'],
            user_id=data['user_id']
        )

        db.session.add(new_board)
        db.session.commit()
        return jsonify({"message": "Board created"}), 200

# /board/<int: board_id>
# 게시글 하나만 불러오기 (GET)
# 게시글 수정하기 (PUT)
# 게시글 삭제하기 (DELETE)
@board_blp.route('/<int:board_id>')
class BoardById(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id) # id = board_id 인것만 query 해오는 코드. 못가져오면 404
        return jsonify(
            {
                "user_id": board.user_id,
                "title": board.title,
                "id": board.id,
                "content": board.content,
                "author": board.author.name
            }
        )

    def put(self, board_id):
        board = Board.query.get_or_404(board_id) # board_id에 해당하는 row를 가져온다.
        data = request.json # 사용자의 request를 json으로 가져온다
        board.title = data['title']
        board.content = data['content']

        db.session.commit()
        return jsonify({"message": "Board updated"}), 200

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"}), 200
