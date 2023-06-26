import os
from pathlib import Path

redpath = os.path.realpath(".")
thispath = os.path.realpath(redpath)

ROOT_PATH = str(Path(thispath))


def get_files(path: str) -> list:
    files = [elt for elt in os.listdir(path) if elt.endswith(".csv")]

    return files
