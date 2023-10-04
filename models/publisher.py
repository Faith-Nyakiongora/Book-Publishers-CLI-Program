from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String
from .base import Base


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

    def __init__(self,name):
        self.name = name