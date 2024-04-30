from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema

# 블루프린트 생성: 'items'라는 이름으로, URL 접두사는 '/items'
blp = Blueprint("items", "items", url_prefix="/items", description="Operations on items")

# 간단한 데이터 저장소 역할을 하는 리스트
items = []


# 'ItemList' 클래스 - GET 및 POST 요청을 처리
@blp.route("/")
class ItemList(MethodView):
    @blp.response(200)
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return items

    @blp.arguments(ItemSchema)
    @blp.response(201, description="Item added")
    def post(self, new_data):
        # 새 아이템을 추가하는 POST 요청 처리
        items.append(new_data)
        return new_data


# 'Item' 클래스 - GET, PUT, DELETE 요청을 처리
@blp.route("/<int:item_id>")
class Item(MethodView):
    @blp.response(200)
    def get(self, item_id):
        # 특정 ID를 가진 아이템을 반환하는 GET 요청 처리
        # next() => 반복문에서 값이 있으면 값을 반환하고 없으면 None을 반환
        # next는 조건을 만족하는 첫 번째 아이템을 반환하고, 그 이후의 아이템은 무시합니다.
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        return item

    @blp.arguments(ItemSchema)
    @blp.response(200, description="Item updated")
    def put(self, new_data, item_id):
        # 특정 ID를 가진 아이템을 업데이트하는 PUT 요청 처리
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        item.update(new_data)
        return item

    @blp.response(204, description="Item deleted")
    def delete(self, item_id):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global items
        if not any(item for item in items if item["id"] == item_id):
            abort(404, message="Item not found")
        items = [item for item in items if item["id"] != item_id]
        return ''