from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, ForeignKey
from .base import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
