import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base
from commands.publisher import add_publisher, list_publishers

# Initialize the database engine and session
DATABASE_URL = "sqlite:///database/book_publisher.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Define a simple CLI loop
def main():
    while True:
        print("Publisher CLI")
        print("1. Add Publisher")
        print("2. List Publishers")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_publisher(session)
        elif choice == "2":
            list_publishers(session)
        elif choice == "0":
            sys.exit("Goodbye!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
