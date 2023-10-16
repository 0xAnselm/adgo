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
