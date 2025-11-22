from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT

class Tone(Base):
    __tablename__ = "tones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(NAME_LENGHT), unique=True, index=True, nullable=False)

    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        return f'Tone{self.name}'