from core.lessons.lessons import Lesson  # Pazi da je 'Lesson' importan u core/lessons/__init__.py
from infrastructure.json_repository import JsonRepository

# Koristimo putanju iz 'tree.txt'
FILE_PATH = 'data_store/files/lessons.json'


class LessonJsonRepository(JsonRepository[Lesson]):
    
    def __init__(self):
        super().__init__(file_path=FILE_PATH, model_class=Lesson)