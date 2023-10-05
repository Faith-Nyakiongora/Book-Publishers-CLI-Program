# from sqlalchemy.orm import relationship
# from sqlalchemy import Integer, Column, String
# from .base import Base


# class Author(Base):
#     __tablename__ = "authors"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     books = relationship("Book", back_populates="author")

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"<Author(name='{self.name}')>"
