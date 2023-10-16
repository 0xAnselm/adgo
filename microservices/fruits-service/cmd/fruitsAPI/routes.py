from flask import jsonify, Blueprint, request
import data.db as fruits_db
import data.models as model

my_routes = Blueprint("my_routes", __name__)


@my_routes.route('/fruits', methods=['GET'])
def get_fruits():
    fruits = [model.Fruit(item['name'], item['color'], item['weight'])
              for item in fruits_db.data]
    return jsonify([fruit.__dict__ for fruit in fruits]), 201


@my_routes.route('/fruits', methods=['POST'])
def add_fruit():
    data = request.get_json()
    if 'name' in data and 'color' in data and 'weight' in data:
        new_fruit = model.Fruit(data['name'], data['color'], data['weight'])
        fruits_db.data.append(
            {'name': new_fruit.name, 'color': new_fruit.color, 'weight': new_fruit.weight})
        return jsonify({'message': 'Fruit added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data. Name, color and weight are required.'}), 400


@my_routes.route('/fruits/<name>', methods=['GET'])
def get_fruit(name):
    for fruit in fruits_db.data:
        if name == fruit['name']:
            return fruit
    return jsonify({'message': f'Fruit {name} not found'}), 404


@my_routes.route('/fruits/<name>', methods=['DELETE'])
def delete_fruit(name):
    for fruit in fruits_db.data:
        if name == fruit['name']:
            fruits_db.data.remove(fruit)
            return jsonify({'message': f'Fruit {name} deleted'}), 200
    return jsonify({'message': f'Fruit {name} not found'}), 404


@my_routes.route('/', methods=['GET'])
@my_routes.route('/ping', methods=['GET'])
@my_routes.route('/<num>', methods=['GET'])
def welcome(num=None):
    if num:
        return jsonify({'message': f'Welcome {num}'})
    else:
        return jsonify({'message': 'Welcome'})
