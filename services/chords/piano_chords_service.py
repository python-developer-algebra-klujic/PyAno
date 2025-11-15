from core.chords.piano_chords import PianoChords
from infrastructure.chords.piano_chords_json_repo import PianoChordsJsonRepository
from services.base_service import BaseService

class PianoChordsService(BaseService[PianoChords]):
    def __init__(self):
        repository = PianoChordsJsonRepository()
        super().__init__(repository)