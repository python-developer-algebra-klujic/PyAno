from core.pianos.pianos import Piano
from infrastructure.json_repository import JsonRepository

# Definiramo putanju do datoteke gdje će se klaviri spremati
PIANOS_JSON_FILE = 'data_store/files/pianos.json'


class PianoJsonRepository(JsonRepository[Piano]):
    """
    Specifični JSON repozitorij za Piano model.
    Nasljeđuje svu logiku iz JsonRepository klase.
    """
    
    def __init__(self):
        """
        Inicijalizator poziva 'super' (roditeljski) konstruktor
        i prosljeđuje mu točno određen model (Piano) i putanju do datoteke.
        """
        super().__init__(file_path=PIANOS_JSON_FILE, model_class=Piano)idemo 