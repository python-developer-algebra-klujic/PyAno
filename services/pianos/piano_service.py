from core.pianos.pianos import Piano
from infrastructure.pianos.piano_json_repo import PianoJsonRepository
from services.base_service import BaseService

class PianoService(BaseService[Piano]):
    def __init__(self):
        # Inicijaliziramo specifični JSON repozitorij
        repository = PianoJsonRepository()
        super().__init__(repository)