from flask import Flask
from dotenv import find_dotenv, load_dotenv
from flask_pymongo import PyMongo
from pymongo import MongoClient

import os

load_dotenv(find_dotenv())
mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password = os.environ.get("MONGO_PWD")

mongo = MongoClient(
    f"mongodb+srv://{mongo_username}:{mongo_password}@cluster0.ejabcra.mongodb.net/?retryWrites=true&w=majority"
)

def main():
    app = Flask(__name__)

    app.config["DEBUG"] = True

    from .routes import routes

    app.register_blueprint(routes)

    return app


if __name__ == "__main__":
    main()
