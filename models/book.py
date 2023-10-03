from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String
from .base import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    