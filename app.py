from config import AppConfig
from infrastructure.base_repository import BaseRepository
from gui import main_menu

def load_config() -> AppConfig:
    return AppConfig()

def main():
    # 1. Inicijaliziraj repozitorije i bazu (ako ne postoje JSON datoteke, kreirat će se)
    BaseRepository()
    # Opcionalno: BaseRepository().db_seed() # Otkomentiraj samo ako želiš ponovno napuniti početnim podacima
    
    # 2. Pokreni Glavni Izbornik (GUI)
    # Ovo je petlja koja će vrtjeti aplikaciju dok korisnik ne izađe
    main_menu()

if __name__ == "__main__":
    main()