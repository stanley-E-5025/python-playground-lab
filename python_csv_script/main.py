import argparse

from script import compare_csv

parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group("required arguments")

required.add_argument(
    "-f",
    "--folder_path",
    type=str,
    required=True,
)

required.add_argument(
    "-sep",
    "--sep_type",
    type=str,
    required=True,
)


console_arguments = parser.parse_args()
folder_path: str = console_arguments.folder_path
sep_type: str = console_arguments.sep_type


def main():
    compare_csv.Compare(folder_path=folder_path, sep_type=sep_type).compare_files()


if __name__ == "__main__":

    main()
