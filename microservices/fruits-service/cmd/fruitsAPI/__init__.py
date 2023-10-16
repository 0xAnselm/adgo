from flask import Flask, request, jsonify
from routes import my_routes
from flask_pymongo import PyMongo

app = Flask(__name__)
app.register_blueprint(my_routes)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/fruitsDB'
mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
