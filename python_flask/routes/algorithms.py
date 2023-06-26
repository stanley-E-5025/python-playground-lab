from flask import Blueprint, render_template, request
from flask_pydantic import validate
from flask_sqlalchemy import SQLAlchemy
from models.algorithms import Algorithm
from settings import token_key
from utils.logger import log_debug, log_info
from validator.algorithms import Algorithms_validator

from python_jwt.modules.validate_jwt import ValidateJWT

algorithms = Blueprint("algorithms", __name__)
db = SQLAlchemy()


# Home page, here you can see all items in the table as a list of cards


@algorithms.route("/algorithms", methods=["GET"])
def get_algorithms() -> str:
    alg = Algorithm.query.all()
    return render_template("index.html", data=alg)


#  Create a new item in the DB


@algorithms.route("/algorithms", methods=["POST"])
@validate(body=Algorithms_validator)
def create_algorithm() -> dict:

    try:
        # body
        data: dict = request.get_json()
        token = request.headers["Authorization"].split(" ")[1]
        validate_jwt: ValidateJWT = ValidateJWT(token=token, secret_key=token_key)
        auth = validate_jwt.validate_token()

        if auth and data:
            # params from body
            complexity: str = data["complexity"]
            name: str = data["name"]
            mathematical_ecuation: str = data["mathematical_ecuation"]
            description: str = data["description"]

            # create a new OBJ model to save
            new_algorithm: dict = Algorithm(
                complexity=complexity,
                name=name,
                mathematical_ecuation=mathematical_ecuation,
                description=description,
            )

            # Save the item in the DB
            db.session.add(new_algorithm)
            db.session.commit()

            # return data & logs
            log_info.info("New Algorithm created! 🚀")
            log_info.debug(f"Algorithm {new_algorithm} added to DB ")
            return {
                "data": data,
            }

        else:

            log_debug.debug(f"item named:{data} require a JWT to be added in the DB")
            log_debug.error("please provide a valid body 🚧")
            return "please provide valid params 🚧"
    except:
        return log_debug.error("Some thing went wrong")


@algorithms.route("/algorithms/<id>", methods=["PATCH"])
def update_algorithms(id) -> str:

    # params from the request
    data: dict = request.get_json()
    token = request.headers["Authorization"].split(" ")[1]
    validate_jwt: ValidateJWT = ValidateJWT(token=token, secret_key=token_key)
    auth = validate_jwt.validate_token()

    if data:

        if auth:

            # body
            alg: dict = Algorithm.query.get(id)

            # params from body
            alg.complexity = data["complexity"]
            alg.name = data["name"]
            alg.mathematical_ecuation = data["mathematical_ecuation"]
            alg.description = data["description"]

            # end connection
            db.session.commit()
            log_info.info("item updated 🚀")

            return "UPDATED"

        else:
            log_debug.debug(f"item named:{id} require a JWT to be added in the DB")
            return "provide a valid token 🚧"

    else:
        log_debug.error("please provide a valid body 🚧")
        return "please provide a valid body 🚧"


@algorithms.route("/algorithms/<id>", methods=["DELETE"])
def delete_algorithms(id) -> str:
    # DB query
    alg: dict = Algorithm.query.get(id)
    token = request.headers["Authorization"].split(" ")[1]
    validate_jwt: ValidateJWT = ValidateJWT(token=token, secret_key=token_key)
    auth = validate_jwt.validate_token()

    if alg:

        if auth:
            # delete the item from the DB
            db.session.delete(alg)
            db.session.commit()

            log_info.info("Algorithm deleted")
            return "DELETE"

        else:
            log_debug.debug(f"item id:{id} require a JWT to be added in the DB")
            return "provide a valid token 🚧"

    else:
        log_debug.error("please provide a valid id 🚧")
        return "please provide a valid id 🚧"
