from flask import Flask, request, jsonify
from routes import my_routes
from flask_pymongo import PyMongo
from data import db
from logger import configure_logger

app = Flask(__name__)
app.register_blueprint(my_routes)

db.connectDB(app)
logger = configure_logger()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
