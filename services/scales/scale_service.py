from core.scales.scales import Scale
from infrastructure.scales.scale_json_repo import ScaleJsonRepository
from services.base_service import BaseService

class ScaleService(BaseService[Scale]):
    def __init__(self):
        repository = ScaleJsonRepository()
        super().__init__(repository)