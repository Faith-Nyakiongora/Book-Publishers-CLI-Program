from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, ForeignKey
from .base import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)