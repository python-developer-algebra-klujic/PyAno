from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False) # Naslov lekcije
    
    description = Column(String(DESCRIPTION_LENGHT), nullable=True) # Sadržaj teksta
    video_url = Column(String(URL_LENGHT), nullable=True) # Link na video
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        return f'Lesson: {self.name}'