import logging

from modules.create_jwt import CreateJWT
from modules.validate_jwt import ValidateJWT
from utils.load_args import load_console_arguments
from utils.logger import load_logger

console_arguments = load_console_arguments()
token: str = console_arguments.token
data: str = console_arguments.data
create: str = console_arguments.create
validate: str = console_arguments.validate
debug: str = console_arguments.debug
key: str = console_arguments.key

load_logger(level=debug)


def main(
    token: str = token,
    data: str = data,
    create: str = create,
    validate: str = validate,
) -> None:

    if create and validate:
        logging.info("You can't create and validate a token at the same time")
    elif create == None and validate == None:
        logging.info("You must specify an action to perform (create or validate) -h for help")

    if validate != None and validate != "true":
        logging.info("Invalid value for validate argument")

    elif validate == "true" and create == None:
        logging.info("Validating token...")
        validate_jwt: ValidateJWT = ValidateJWT(token=token, secret_key=key)
        validate_jwt.validate_token()

    if create != None and create != "true":
        logging.info("Invalid value for create argument")

    elif create == "true" and validate == None:
        create_jwt: CreateJWT = CreateJWT(expiration=3600, data=data, secret_key=key)
        create_jwt.create_token()


if __name__ == "__main__":
    main()
