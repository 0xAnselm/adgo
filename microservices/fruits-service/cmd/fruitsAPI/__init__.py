from flask import Flask, jsonify
from flask_pymongo import PyMongo
from data import db
import routes
from logger import configure_logger

logger = configure_logger()

app = Flask(__name__)
app.register_blueprint(routes.my_routes)

app.config['MONGO_HOST'] = 'mongo-fruits'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'fruitsDB'
app.config['MONGO_USERNAME'] = 'admin'
app.config['MONGO_PASSWORD'] = 'password'
app.config['MONGO_AUTH_SOURCE'] = 'admin'

app.config['MONGO_URI'] = "mongodb://%s:%s@%s:%s/%s?authSource=%s" % (
    app.config['MONGO_USERNAME'],
    app.config['MONGO_PASSWORD'],
    app.config['MONGO_HOST'],
    app.config['MONGO_PORT'],
    app.config['MONGO_DBNAME'],
    app.config['MONGO_AUTH_SOURCE']
)

mongo = PyMongo(app)


@app.route('/diag', methods=['GET'])
def diag():
    logger.info(app.config)
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90, debug=True)
