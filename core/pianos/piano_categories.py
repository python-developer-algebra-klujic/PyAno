from sqlalchemy import Column, Integer

from infrastructure.database.database import Base


class PianoCategory(Base):
    __tablename__ = 'piano-category'

    id = Column(Integer)




    # ACOUSTIC = "acoustic"
    # ELECTRIC = "electric"
    # GRAND = "grand"
    # UPRIGHT = "upright"
    # DIGITAL = "digital"
    # HYBRID = "hybrid"
