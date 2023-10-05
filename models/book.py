# from sqlalchemy.orm import relationship
# from sqlalchemy import Integer, Column, String, ForeignKey
# from .base import Base


# class Book(Base):
#     __tablename__ = "books"
#     id = Column(Integer, primary_key=True)
#     title = Column(String)

#     publisher_id = Column(Integer, ForeignKey("publishers.id"))
#     author_id = Column(Integer, ForeignKey("authors.id"))

#     publisher = relationship("Publisher", back_populates="books")
#     author = relationship("Author", back_populates="books")

#     def __init__(self, title: str, publisher, author):
#         self.title = title
#         self.publisher = publisher
#         self.author = author
