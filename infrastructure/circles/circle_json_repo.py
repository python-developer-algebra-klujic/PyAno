from core.circles.circles import Circle  # Pazi da je 'Circle' importan u core/circles/__init__.py
from infrastructure.json_repository import JsonRepository

# Koristimo putanju iz 'tree.txt'
FILE_PATH = 'data_store/files/circles.json'


class CircleJsonRepository(JsonRepository[Circle]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=Circle)