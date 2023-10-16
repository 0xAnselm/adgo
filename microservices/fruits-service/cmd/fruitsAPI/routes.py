import data.db as fruits_db
from data.models import Fruit
from flask import jsonify, Blueprint, request
import data.models as model
from logger import configure_logger

my_routes = Blueprint("my_routes", __name__)
logger = configure_logger()  # Initialize the logger


@my_routes.route('/fruits', methods=['GET'])
def get_fruits():
    pass


@my_routes.route('/fruits', methods=['POST'])
def add_fruit():
    data = request.get_json()

    if 'name' in data and 'color' in data and 'weight' in data:
        new_fruit = {
            'name': data['name'],
            'color': data['color'],
            'weight': data['weight']
        }

        fruits_db.mongo.db.fruits.insert_one(new_fruit)
        return jsonify({'message': 'Fruit added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data. Name, color, and weight are required.'}), 400


@my_routes.route('/fruits/<name>', methods=['GET'])
def get_fruit(name):
    logger.info('Hello world!')
    cherry = fruits_db.mongo.db.fruits.find({'name': 'cherry'})
    return jsonify({'message': 'fuck'})


@my_routes.route('/fruits/<name>', methods=['DELETE'])
def delete_fruit(name):
    for fruit in fruits_db.data:
        if name == fruit['name']:
            fruits_db.data.remove(fruit)
            return jsonify({'message': f'Fruit {name} deleted'}), 200
    return jsonify({'message': f'Fruit {name} not found'}), 404


@my_routes.route('/', methods=['GET'])
@my_routes.route('/<num>', methods=['GET'])
def welcome(num=None):
    if num:
        return jsonify({'message': f'Welcome {num}'})
    else:
        return jsonify({'message': 'Welcome'})


@my_routes.route('/ping', methods=['GET'])
def test_db_connection():
    try:
        fruits_db.mongo.db.command('ping')
        return jsonify({'message': 'Database connection is active'}), 200
    except Exception as e:
        return jsonify({'error': 'Database connection error', 'message': str(e)}), 500
