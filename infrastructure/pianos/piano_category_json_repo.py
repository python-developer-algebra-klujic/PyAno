from core.pianos.piano_categories import PianoCategory
from infrastructure.json_repository import JsonRepository

FILE_PATH = 'data_store/files/piano_categories.json'


class PianoCategoryJsonRepository(JsonRepository[PianoCategory]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=PianoCategory)