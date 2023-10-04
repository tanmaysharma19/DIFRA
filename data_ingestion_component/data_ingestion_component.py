# data_ingestion_component/data_ingestion_component.py
import config
from data_lake_storage.data_lake_storage import DataLakeStorage

class DataIngestionComponent:
    def __init__(self, data_lake_storage):
        self.data_lake_storage = data_lake_storage

    def ingest_data(self):
        # Simulate data ingestion and preprocessing
        print(config.GREEN + "\nIngesting and preprocessing data..." + config.RESET)
        
        # Download a file from Data Lake
        # self.data_lake_storage.download_file('remote_file.txt', 'local_file.txt')
        self.data_lake_storage.download_file('data.csv', 'local_data.csv')

        # Upload processed data back to Data Lake
        # self.data_lake_storage.upload_file('local_processed_file.txt', 'remote_processed_file.txt')
        print("Data ingestion and preprocessing completed.")

def main():
    # Initialize Data Lake Storage
    data_lake_storage = DataLakeStorage(config.DATA_LAKE_STORAGE_DIRECTORY)

    # Initialize Data Ingestion Component
    data_ingestion_component = DataIngestionComponent(data_lake_storage)

    # # Run data ingestion
    # data_ingestion_component.ingest_data()

if __name__ == "__main__":
    main()
