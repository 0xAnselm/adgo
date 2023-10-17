from flask import jsonify, Blueprint, request
from logger import configure_logger
import data.db as fruits_db

my_routes = Blueprint("my_routes", __name__)
logger = configure_logger()  # Initialize the logger


@my_routes.route('/fruits', methods=['GET'])  # Get all fruits
def get_fruits():
    return fruits_db.find_all()


@my_routes.route('/fruits', methods=['POST'])  # Add a fruit
def add_fruit():
    data = request.get_json()
    return fruits_db.add_fruit(data)


@my_routes.route('/fruits/<name>', methods=['GET'])  # Get fruit by name
def get_fruit(name):
    return fruits_db.get_fruit(name)


@my_routes.route('/fruits/<name>', methods=['DELETE'])
def delete_fruit(name):
    return fruits_db.delete_fruit(name)


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
