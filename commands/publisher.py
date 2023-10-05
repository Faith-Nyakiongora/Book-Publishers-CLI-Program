from main import Publisher


def add_publisher(session):
    name = input("Enter publisher name: ")
    publisher = Publisher(name=name)
    session.add(publisher)
    session.commit()
    print(f"Added publisher: {name}")


def list_publishers(session):
    publishers = session.query(Publisher).all()
    for publisher in publishers:
        print(f"ID: {publisher.id}, Name: {publisher.name}")
