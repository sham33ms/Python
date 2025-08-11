from db import Base, engine
from models import Subscriber, Newsletter, Engagement
import services

# Create tables if not exist
Base.metadata.create_all(engine)

def main():
    while True:
        print("\n--- Newsletter Management ---")
        print("1. Add Subscriber")
        print("2. Remove Subscriber")
        print("3. Send Newsletter")
        print("4. Record Engagement")
        print("5. Export Subscribers to CSV")
        print("6. Import Subscribers from JSON")
        print("7. Analyze Performance")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            services.add_subscriber()
        elif choice == "2":
            services.remove_subscriber()
        elif choice == "3":
            services.send_newsletter()
        elif choice == "4":
            services.record_engagement()
        elif choice == "5":
            services.export_subscribers()
        elif choice == "6":
            services.import_subscribers()
        elif choice == "7":
            services.analyze()
        elif choice == "8":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
