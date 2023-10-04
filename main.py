# main.py
import subprocess
from data_lake_storage.data_lake_storage import DataLakeStorage
from data_ingestion_scheduler.data_ingestion_scheduler import DataIngestionScheduler
from data_ingestion_component.data_ingestion_component import DataIngestionComponent
from data_aggregator.data_aggregator import DataAggregator
from data_repository.data_repository import DataRepository
from reporting_and_visualization.reporting_and_visualization import ReportingAndVisualization
from notification_service.notification_service import NotificationService
import config
import sys
import os


def main():
    # Initialize Data Lake storage
    data_lake_storage = DataLakeStorage(config.DATA_LAKE_STORAGE_DIRECTORY)

    # Initialize Data Ingestion Scheduler
    data_ingestion_scheduler = DataIngestionScheduler()

    # Initialize Data Ingestion Component
    data_ingestion_component = DataIngestionComponent(data_lake_storage)

    # Initialize Data Aggregator Component
    data_aggregator = DataAggregator(data_lake_storage)

    # Initialize Data Repository
    data_repository = DataRepository()

    # Initialize Reporting and Visualization component
    reporting_and_visualization = ReportingAndVisualization()

    # Initialize Notification Service Component
    notification_service = NotificationService()

    # Run Data Lake Storage methods
    files = data_lake_storage.list_files()
    print(config.GREEN + "\nFiles in Data Lake:" + str(files) + config.RESET)

    # Schedule data ingestion
    data_ingestion_scheduler.schedule_ingestion(data_ingestion_component)

    # Aggregate spending data
    aggregated_data = data_aggregator.aggregate_spending(config.INPUT_FILE_PATH)
    print(config.GREEN + "\nPrinting aggregated data..." + config.RESET)
    print(aggregated_data)

    # Store aggregated data
    data_repository.store_data(aggregated_data)

    # Generate a report
    reporting_and_visualization.generate_report(aggregated_data)

    # Generate visualizations
    reporting_and_visualization.generate_visualizations(aggregated_data)

    # Send a notification
    notification_service.send_notification(
        "\nOctober 2023 GCP Spend Report Generated.")


if __name__ == "__main__":
    main()
