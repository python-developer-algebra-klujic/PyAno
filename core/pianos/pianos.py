from sqlalchemy import Column, Integer, ForeignKey

from infrastructure.database.database import Base


class Piano(Base):
    __tablename__ = 'piano'

    id = Column(Integer)

    piano_category_id = ForeignKey()
