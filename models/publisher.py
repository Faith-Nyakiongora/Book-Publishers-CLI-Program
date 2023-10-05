# from sqlalchemy.orm import relationship
# from sqlalchemy import Integer, Column, String
# from .base import Base


# class Publisher(Base):
#     __tablename__ = "publishers"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     # Relationship one to many
#     books = relationship("Book", back_populates="publisher")

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"<Publisher(name='{self.name}')>"
