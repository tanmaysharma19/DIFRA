# data_lake_storage/data_lake_storage.py
import os

class DataLakeStorage:
    def __init__(self, storage_directory):
        self.storage_directory = storage_directory

    def upload_file(self, local_file_path, remote_file_path):
        # Simulating uploading a file to the Data Lake
        try:
            with open(local_file_path, 'rb') as local_file, open(f"{self.storage_directory}/{remote_file_path}", 'wb') as remote_file:
                remote_file.write(local_file.read())
            print(f"Uploaded {local_file_path} to {remote_file_path}")
        except FileNotFoundError:
            print(f"File not found: {local_file_path}")

    def list_files(self):
        # Simulating listing files in the Data Lake
        return os.listdir(self.storage_directory)

    def download_file(self, remote_file_path, local_file_path):
        # Simulating downloading a file from the Data Lake
        try:
            with open(f"{self.storage_directory}/{remote_file_path}", 'rb') as remote_file, open(local_file_path, 'wb') as local_file:
                local_file.write(remote_file.read())
            print(f"Downloaded {remote_file_path} to {local_file_path}")
        except FileNotFoundError:
            print(f"File not found: {remote_file_path}")

    def delete_file(self, remote_file_path):
        # Simulating deleting a file from the Data Lake
        try:
            os.remove(f"{self.storage_directory}/{remote_file_path}")
            print(f"Deleted {remote_file_path} from the Data Lake")
        except FileNotFoundError:
            print(f"File not found: {remote_file_path}")