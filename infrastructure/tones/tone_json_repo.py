from core.tones.tones import Tone  # Pazi da je 'Tone' importan u core/tones/__init__.py
from infrastructure.json_repository import JsonRepository

# Koristimo putanju iz 'tree.txt'
FILE_PATH = 'data_store/files/tones.json'


class ToneJsonRepository(JsonRepository[Tone]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=Tone)