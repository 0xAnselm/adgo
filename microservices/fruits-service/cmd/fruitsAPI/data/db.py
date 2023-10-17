import data.db as fruits_db
from data.models import Fruit
from flask_pymongo import PyMongo
from flask import jsonify
from logger import configure_logger

mongo = PyMongo()
logger = configure_logger()  # Initialize the logger


def connectDB(app):
    app.config['MONGO_URI'] = "mongodb://admin:password@localhost:27018/db_name?authSource=admin"
    mongo.init_app(app)


def error():
    return jsonify({'error': True, 'message': 'error'}), 500


def find_all():
    result = fruits_db.mongo.db.fruits.find({})
    logger.info(result)
    d = []
    for r in result:
        d.append(Fruit(**r).to_json())
    return jsonify(d)


def add_fruit(data: any):
    if 'name' in data and 'color' in data and 'weight' in data:
        new_fruit = Fruit(data['name'], data['color'], data['weight'])
        fruits_db.mongo.db.fruits.insert_one(new_fruit.to_json())
        return jsonify({'message': 'Fruit added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data. Name, color, and weight are required.'}), 400


def get_fruit(name: str):
    fruit = fruits_db.mongo.db.fruits.find_one_or_404({'name': name})
    return Fruit(**fruit).to_json()


def delete_fruit(name: str):
    fruit = fruits_db.mongo.db.fruits.find_one({'name': name})

    if fruit is None:
        logger.info(f'Fruit {name} not found')
        return jsonify({'message': f'Fruit {name} not found'}), 404

    fruits_db.mongo.db.fruits.delete_one({'name': name})

    logger.info(f'Fruit {name} deleted')
    return jsonify({'message': f'Fruit {name} deleted'}), 200
