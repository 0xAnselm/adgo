import data.db as fruits_db
from flask import jsonify, Blueprint, request
from bson.json_util import dumps
from data.models import Fruit
import data.db
from logger import configure_logger

my_routes = Blueprint("my_routes", __name__)
logger = configure_logger()  # Initialize the logger


@my_routes.route('/fruits', methods=['GET'])  # Get all fruits
def get_fruits():
    return data.db.find_all()


@my_routes.route('/fruits', methods=['POST'])  # Add a fruit
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


@my_routes.route('/fruits/<name>', methods=['GET'])  # Get fruit by name
def get_fruit(name):
    fruit = fruits_db.mongo.db.fruits.find_one_or_404({'name': name})
    return Fruit(**fruit).to_json()


@my_routes.route('/fruits/<name>', methods=['DELETE'])
def delete_fruit(name):
    fruit = fruits_db.mongo.db.fruits.find_one({'name': name})

    if fruit is None:
        logger.info(f'Fruit {name} not found')
        return jsonify({'message': f'Fruit {name} not found'}, 404)

    fruits_db.mongo.db.fruits.delete_one({'name': name})

    logger.info(f'Fruit {name} deleted')
    return jsonify({'message': f'Fruit {name} deleted'}), 200


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
