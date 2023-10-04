# notification_service/notification_service.py
import config

class NotificationService:
    def __init__(self):
        # Initialize the Notification Service component
        pass

    def send_notification(self, message):
        # Simulate sending a notification
        print(config.YELLOW + "\nSending notification..." + config.RESET)
        
        print("Notification sent.")

def main():
    # Initialize Notification Service component
    notification_service = NotificationService()

    notification_service.send_notification("Data processing completed.")

if __name__ == "__main__":
    main()
