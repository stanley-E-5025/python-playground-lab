from database.db import create_tables
from flask import Flask
from routes.notes import notes


def create_app():
    app = Flask(__name__)
    create_tables()
    app.register_blueprint(notes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3000, debug=True)
