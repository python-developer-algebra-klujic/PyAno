from core.pianos.piano_types import PianoType
from infrastructure.json_repository import JsonRepository

FILE_PATH = 'data_store/files/piano_types.json'


class PianoTypeJsonRepository(JsonRepository[PianoType]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=PianoType)