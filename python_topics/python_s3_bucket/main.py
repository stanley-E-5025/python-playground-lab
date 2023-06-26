import io
import json
import os
import pathlib
import shutil
import subprocess
from pathlib import Path

import boto3
import pandas as pd
import pyarrow
import pyarrow.parquet as pq
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3_connection = boto3.resource(
    service_name="s3",
    region_name="us-east-2",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
)

def write_to_s3(file_path, file_name, file_type):
    try:
        if not pathlib.Path(file_path).exists():
            raise ValueError(f"{file_path} does not exist.")
        if file_type in ['.mp4', '.mkv', '.flv', '.avi']:
            video_extensions = ['.mp4', '.mkv', '.flv', '.avi']
            if not file_path.endswith(tuple(video_extensions)):
              raise ValueError(f"Invalid video format, only {video_extensions} are supported.")
            # handle video file
            subprocess.run(["ffmpeg", "-i", file_path, "-vf", "fps=30", "compressed_video.mp4"])
            s3_connection.Bucket(BUCKET_NAME).upload_file(Filename="compressed_video.mp4", Key=file_name)
        else:
            s3_connection.Bucket(BUCKET_NAME).upload_file(Filename=file_path, Key=file_name)
        print("File saved to S3 📦")
    except Exception as error:
        print(error)

def read_from_s3(file_name, file_type, save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        obj = s3_connection.Bucket(BUCKET_NAME).Object(file_name).get()
        with open(os.path.join(save_path, file_name), "wb") as f:
            shutil.copyfileobj(obj["Body"], f)
        print(f"{file_type} file from S3 🗂 saved to {save_path}")
    except Exception as error:
        print(error)


def handle_read_file(folder_path:str,files: list) -> None:
    for file in files:
        file_name = file
        file_type = file.split(".")[-1]
        read_from_s3(file_name, file_type, folder_path)

def handle_write_file(folder_path:str,files: list) -> None:
    for file in files:
        file_path = f"{folder_path}/{file}"
        file_name = file
        file_type = file.split(".")[-1]
        write_to_s3(file_path, file_name, file_type)

def main() -> None:

    path_to_write = f"{Path.cwd()}/python_topics/python_s3_bucket"
    path_to_read = f"{Path.cwd()}/python_topics/python_s3_bucket/test_dowload_files"

    files_to_write = [elt for elt in os.listdir(path_to_write)]
    files_to_read = ["video.mp4", "hello.txt"]

    handle_write_file(path_to_write,files_to_write)
    handle_read_file(path_to_read,files_to_read)

   

if __name__ == "__main__":
    main()
