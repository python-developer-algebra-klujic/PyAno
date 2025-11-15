from core.circles.circles import Circle
from infrastructure.circles.circle_json_repo import CircleJsonRepository
from services.base_service import BaseService

class CircleService(BaseService[Circle]):
    def __init__(self):
        repository = CircleJsonRepository()
        super().__init__(repository)