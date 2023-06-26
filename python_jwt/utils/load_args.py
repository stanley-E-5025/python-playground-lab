import argparse


def load_console_arguments():
    """Loads the console arguments"""
    parser = argparse.ArgumentParser(description="Performs validation controls on Prophet input files")

    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    optional = parser.add_argument_group("optional arguments")

    optional.add_argument(
        "-t",
        "--token",
        help="provide a token to validate",
        type=str,
        required=False,
    )

    optional.add_argument(
        "--data",
        help="add a valid username",
        type=str,
        required=False,
    )

    optional.add_argument(
        "-k",
        "--key",
        help="secret key to use",
        type=str,
        required=False,
    )

    optional.add_argument(
        "-v",
        "--validate",
        help="only validate a token",
        type=str,
        required=False,
    )

    optional.add_argument(
        "-c",
        "--create",
        help="create a token",
        type=str,
        required=False,
    )

    optional.add_argument("-d", "--debug", help="show debug info", type=str, required=False, default=False)

    return parser.parse_args()
