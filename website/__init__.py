from flask import Flask


def main():
    app = Flask(__name__)

    from .routes import routes

    app.register_blueprint(routes)

    return app


if __name__ == "__main__":
    main()
