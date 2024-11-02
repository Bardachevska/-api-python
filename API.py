from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)  # Create an Api object

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return jsonify(item)
        return {'message': 'Item not found'}, 404

    def post(self):
        data = request.get_json()
        new_item = {
            'name': data['name'],
            'price': data['price'],
        }
        items.append(new_item)
        return jsonify(new_item)

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}

# Add the resource routes
api.add_resource(Item, '/item/<string:name>', '/item')

if __name__ == '__main__':
    app.run(debug=True)
