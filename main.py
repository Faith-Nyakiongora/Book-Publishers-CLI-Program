# Import SQLAlchemy and create the engine and session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Define your model classes before creating the engine
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship one to many
    books = relationship("Book", back_populates="publisher")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Publisher(name='{self.name}')>"


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f"<Author(name='{self.name}')>"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)

    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    author_id = Column(Integer, ForeignKey("authors.id"))

    publisher = relationship("Publisher", back_populates="books")
    author = relationship("Author", back_populates="books")

    def __init__(self, title: str, publisher, author):
        self.title = title
        self.publisher = publisher
        self.author = author


# Define the database URL
DATABASE_URL = "sqlite:///book_publisher.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables in the database
Base.metadata.create_all(engine)
