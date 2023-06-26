from flask import Blueprint
from steps.load import load_notes

notes = Blueprint("notes", __name__)


@notes.route("/notes", methods=["GET"])
def get_notes():
    return load_notes()
