from flask import request
from flask_restful import Resource

items = []  # 임시 DB


class Item(Resource):

    # HTTP GET (READ)
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"message": "Item not found"}, 404  # msg, code

    # HTTP POST (CREATE)
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg": "Item already exists"}, 404  # msg, code

        data = request.get_json()
        new_item = {'name': data['name'], 'price': data['price']}
        items.append(new_item)

        return new_item

    # HTTP PUT (UPDATE)
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item

        # 만약 업데이트하고자하는 아이템 데이터가 없다면, 추가
        new_item = {'name': data['name'], 'price': data['price']}
        items.append(new_item)

        return new_item

    # HTTP DELETE
    def delete(self, name):
        global items

        items = [item for item in items if item['name'] != name]

        return {'msg': 'Item deleted'}