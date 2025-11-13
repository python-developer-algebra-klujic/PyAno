from .database.database import Base, engine, Session
from infrastructure.pianos.piano_category_repo import PianoCategoryRepository


class BaseRepository:
    def __init__(self):
        Base.metadata.create_all(engine)

        self.piano_category_repo = PianoCategoryRepository(Session)
