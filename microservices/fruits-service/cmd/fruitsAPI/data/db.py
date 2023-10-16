from flask_pymongo import PyMongo

mongo = PyMongo()


def connectDB(app):
    app.config['MONGO_URI'] = "mongodb://admin:password@localhost:27018/db_name?authSource=admin"
    mongo.init_app(app)
