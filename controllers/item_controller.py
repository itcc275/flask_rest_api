# type: ignore
from flask import Blueprint, request, jsonify
from services.item_servie import ItemService

item_controller = Blueprint('item_controller', __name__)
service = ItemService()

#create item
@item_controller.route('/items', methods=['POST']) 
def create_item():
    data = request.json
    item = service.create_item(data["name"], data["description"])
    return jsonify(item.to_dict()), 201

#get all items
@item_controller.route('/items', methods=['GET'])
def get_items():
    items = service.get_all_items()
    return jsonify(items), 200

#get item by id
@item_controller.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = service.get_item_by_id(item_id)
    return jsonify(item), 200 if item else (jsonify({"error": "Item not found"}), 404)

#update item
@item_controller.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = service.update_item(item_id, data["name"], data["description"])
    return jsonify(item), 200 if item else (jsonify({"error": "Item not found"}), 404)

#delete item
@item_controller.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if service.delete_item(item_id):
        return jsonify({"message": "Item deleted"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404
# The above code defines a Flask blueprint for item management, including routes for creating, retrieving, updating, and deleting items.
# The controller uses the ItemService to handle the business logic and interact with the repository.
# The routes are defined with appropriate HTTP methods and return JSON responses with the relevant status codes.
# The controller is registered with the Flask application in the main app file.