from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT


class Scale(Base):
    __tablename__ = 'scales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False) # Npr. "C Major", "A Minor"
    
    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        return f'Scale: {self.name}'