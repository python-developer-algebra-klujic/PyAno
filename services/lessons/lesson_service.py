from core.lessons.lessons import Lesson
from infrastructure.lessons.lesson_json_repo import LessonJsonRepository
from services.base_service import BaseService

class LessonService(BaseService[Lesson]):
    def __init__(self):
        repository = LessonJsonRepository()
        super().__init__(repository)