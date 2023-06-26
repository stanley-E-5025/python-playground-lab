from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.algorithms import algorithms

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    SQLAlchemy(app)

    app.register_blueprint(algorithms)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5050, debug=True)
