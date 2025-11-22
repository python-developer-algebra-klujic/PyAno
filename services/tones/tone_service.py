from core.tones.tones import Tone
from infrastructure.tones.tone_json_repo import ToneJsonRepository
from services.base_service import BaseService

class ToneService(BaseService[Tone]):
    def __init__(self):
        repository = ToneJsonRepository()
        super().__init__(repository)