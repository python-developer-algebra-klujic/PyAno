from typing import List
from sqlalchemy.orm import Session

from core.pianos.piano_categories import PianoCategory


class PianoCategoryRepository:
    def __init__(self, Session: Session):
        self.Session = Session

    def get(self, piano_category_id: int) -> PianoCategory:
        with self.Session() as session:
            return session.query(PianoCategory).filter_by(id = piano_category_id).first()

    def get_all(self) -> List[PianoCategory]:
        with self.Session() as session:
            return session.query(PianoCategory).all()

    def add(self, piano_category: PianoCategory) -> PianoCategory:
        with self.Session() as session:
            piano_category_from_db = self.get(piano_category.id)
            if not piano_category_from_db:
                session.add(piano_category)
                session.commit()
                return piano_category
            else:
                return None

    def update(self, piano_category: PianoCategory) -> PianoCategory:
        with self.Session() as session:
            piano_category_from_db = self.get(piano_category.id)
            if piano_category_from_db:
                piano_category_from_db = piano_category
                session.commit()
                return piano_category
            else:
                return None

    def delete(self, piano_category_id: int):
        with self.Session() as session:
            piano_category_from_db = self.get(piano_category_id)
            if piano_category_from_db:
                session.delete(piano_category_from_db)
                session.commit()


