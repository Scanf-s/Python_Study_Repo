from flask import Flask
from flask_restful import Api
from resources import Item
app = Flask(__name__)
api = Api(app)


api.add_resource(Item, '/item/<string:name>')
