from core.chords.piano_chords import PianoChords
from infrastructure.json_repository import JsonRepository

# Koristimo putanju iz 'tree.txt'
FILE_PATH = 'data_store/files/chords.json'


class PianoChordsJsonRepository(JsonRepository[PianoChords]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=PianoChords)