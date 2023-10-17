from data.models import Fruit
from fruitsAPI import mongo
from flask import jsonify
from logger import configure_logger

logger = configure_logger()  # Initialize the logger


def error():
    return jsonify({'error': True, 'message': 'error'}), 500


def find_all():
    result = mongo.db.fruits.find({})
    logger.info(result)
    d = []
    for r in result:
        d.append(Fruit(**r).to_json())
    return jsonify(d)


def add_fruit(data: any):
    if 'name' in data and 'color' in data and 'weight' in data:
        new_fruit = Fruit(data['name'], data['color'], data['weight'])
        mongo.db.fruits.insert_one(new_fruit.to_json())
        return jsonify({'message': 'Fruit added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data. Name, color, and weight are required.'}), 400


def get_fruit(name: str):
    fruit = mongo.db.fruits.find_one_or_404({'name': name})
    return Fruit(**fruit).to_json()


def delete_fruit(name: str):
    fruit = mongo.db.fruits.find_one({'name': name})

    if fruit is None:
        logger.info(f'Fruit {name} not found')
        return jsonify({'message': f'Fruit {name} not found'}), 404

    mongo.db.fruits.delete_one({'name': name})

    logger.info(f'Fruit {name} deleted')
    return jsonify({'message': f'Fruit {name} deleted'}), 200
