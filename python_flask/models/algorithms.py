from ast import arg

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Algorithm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complexity = db.Column(db.String(200))
    name = db.Column(db.String(200))
    mathematical_ecuation = db.Column(db.String(200))
    description = db.Column(db.String(200))


def __init__(self, complexity, name, mathematical_ecuation, description) -> arg:
    self.complexity = complexity
    self.name = name
    self.mathematical_ecuation = mathematical_ecuation
    self.description = description
