# data_ingestion_scheduler/data_ingestion_scheduler.py
import config

class DataIngestionScheduler:
    def __init__(self):
        # Initialize the Data Ingestion Scheduler
        pass

    def schedule_ingestion(self, data_ingestion_component):
        # Simulating scheduling data ingestion
        print(config.YELLOW + "\nScheduling data ingestion..." + config.RESET)
        
        # Call the Data Ingestion Component
        data_ingestion_component.ingest_data()      

def main():
    # Initialize the Data Ingestion Scheduler
    data_ingestion_scheduler = DataIngestionScheduler()

    # Scheduling data ingestion
    # data_ingestion_scheduler.schedule_ingestion(data_ingestion_component)

if __name__ == "__main__":
    main()
