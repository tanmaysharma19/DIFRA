# data_repository/data_repository.py
import config

class DataRepository:
    def __init__(self):
        # Initialize the Data Repository
        pass

    def store_data(self, aggregated_data):
        # Simulate storing aggregated data
        print(config.GREEN + "\nStoring aggregated data @ " + config.YELLOW + config.DATA_REPOSITORY_SETTINGS['local_data_repository_path'] + '/aggregated_data.csv' + config.RESET)
        
        # Saving the aggregated data to a new CSV file (in Phase 2 we can move to cloud storage like S3, etc.)
        aggregated_data.to_csv(config.DATA_REPOSITORY_SETTINGS['local_data_repository_path'] + '/aggregated_data.csv', index=False)
        
        print("Aggregated data stored.")

def main():
    # Initialize Data Repository
    data_repository = DataRepository()

    # # Store aggregated data
    # data_repository.store_data(aggregated_data)

if __name__ == "__main__":
    main()
