from core.pianos.piano_categories import PianoCategory
from infrastructure.pianos.piano_category_json_repo import PianoCategoryJsonRepository
from services.base_service import BaseService

class PianoCategoryService(BaseService[PianoCategory]):
    def __init__(self):
        repository = PianoCategoryJsonRepository()
        super().__init__(repository)