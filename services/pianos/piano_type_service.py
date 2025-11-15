from core.pianos.piano_types import PianoType
from infrastructure.pianos.piano_type_json_repo import PianoTypeJsonRepository
from services.base_service import BaseService

class PianoTypeService(BaseService[PianoType]):
    def __init__(self):
        repository = PianoTypeJsonRepository()
        super().__init__(repository)