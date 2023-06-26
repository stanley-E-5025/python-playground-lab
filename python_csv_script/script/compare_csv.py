import pandas as pd
from utils import ROOT_PATH, get_files


class Compare:
    def __init__(self, folder_path: str, sep_type: str) -> None:
        self.folder_path: str = f"{ROOT_PATH}/files/{folder_path}"
        self.sep_type: str = sep_type

    def compare_files(self) -> bool:
        """
        A python script that can take TWO paths/CSVs files and compare if they are EQUAL in all matrix values/positions columns
        """

        files = get_files(self.folder_path)
        result: bool = True

        col_frame_a: list = pd.read_csv(
            f"{self.folder_path}/{files[0]}", sep=self.sep_type
        ).columns.to_list()

        col_frame_b: list = pd.read_csv(
            f"{self.folder_path}/{files[1]}", sep=self.sep_type
        ).columns.to_list()

        for columns_a, columns_b in zip(col_frame_a, col_frame_b):

            data_frame_a: list = pd.read_csv(
                f"{self.folder_path}/{files[0]}", sep=self.sep_type
            )[columns_a].to_list()

            data_frame_b: list = pd.read_csv(
                f"{self.folder_path}/{files[1]}", sep=self.sep_type
            )[columns_b].to_list()

            if not data_frame_a == data_frame_b:
                result = False

        print(result)
        return result
