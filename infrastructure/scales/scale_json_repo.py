from core.scales.scales import Scale  # Pazi da je 'Scale' importan u core/scales/__init__.py
from infrastructure.json_repository import JsonRepository

# Koristimo putanju iz 'tree.txt'
FILE_PATH = 'data_store/files/scales.json'


class ScaleJsonRepository(JsonRepository[Scale]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=Scale)