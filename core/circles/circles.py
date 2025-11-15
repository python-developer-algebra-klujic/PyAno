from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT


class Circle(Base):
    __tablename__ = 'circles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False) # Npr. "Circle of Fifths"
    
    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        return f'Circle: {self.name}'