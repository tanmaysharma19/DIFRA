# config.py

# data lake storage directory (local or cloud in phase 2)
DATA_LAKE_STORAGE_DIRECTORY = '/Users/tanmaysharma/Desktop/Final/DIFRA/DIFRA/data_lake_storage/data'

INPUT_FILE_PATH = DATA_LAKE_STORAGE_DIRECTORY + '/data.csv'

# data ingestion schedule interval (in phase 2)
DATA_INGESTION_SCHEDULE_INTERVAL = '0 0 * * *'  # Daily schedule at midnight (Cron format)

# data aggregation interval (in phase 2)
DATA_AGGREGATION_INTERVAL = '0 0 * * *'  # Daily schedule at midnight (Cron format)

# data repository settings (e.g., database connection details, cloud storage credentials, etc.)
DATA_REPOSITORY_SETTINGS = {
    'local_data_repository_path':'/Users/tanmaysharma/Desktop/Final/DIFRA/DIFRA/data_repository/data',
    'database_url': 'database_url',
    'cloud_storage_credentials': 'cloud_storage_credentials',
}

# notification settings (e.g., email server details, messaging service credentials, etc.)
NOTIFICATION_SETTINGS = {
    'email_server': 'email_server',
    'email_credentials': 'email_credentials',
    'messaging_service_credentials': 'messaging_service_credentials',
}

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

