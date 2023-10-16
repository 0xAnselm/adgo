from flask import Flask, request, jsonify
from routes import my_routes
import logging

app = Flask(__name__)
app.register_blueprint(my_routes)

data = [
    {'name': 'apple', 'color': 'red'},
    {'name': 'banana', 'color': 'yellow'},
    {'name': 'cherry', 'color': 'red'}
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
