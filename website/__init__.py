from flask import Flask
from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient

import os

load_dotenv(find_dotenv())
mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password = os.environ.get("MONGO_PWD")

print(mongo_username)
print(mongo_password)

mongo = MongoClient(
    f"mongodb+srv://lukebing:IK0Mm3dh4JyrsgDs@cluster0.ejabcra.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
)

def main():
    app = Flask(__name__)

    app.config["DEBUG"] = True

    from .routes import routes

    app.register_blueprint(routes)

    return app


if __name__ == "__main__":
    main()
