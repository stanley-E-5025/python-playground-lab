import logging


def load_logger(level):
    level = logging.DEBUG if level else logging.INFO
    logging.basicConfig(format="%(levelname)s %(filename)s:%(lineno)s %(funcName)20s() %(message)s", level=level)
