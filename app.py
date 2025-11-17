from config import AppConfig
from infrastructure.base_repository import BaseRepository
from gui.main_menu import main_menu

def load_config() -> AppConfig:
    return AppConfig()

def main():
    # 1. Učitaj konfiguraciju
    config = load_config()
    
    # 2. Inicijaliziraj repozitorije i bazu (ako ne postoje JSON datoteke, kreirat će se)
    repo = BaseRepository()
    # Opcionalno: repo.db_seed() # Otkomentiraj samo ako želiš ponovno napuniti početnim podacima
    
    # 3. Pokreni Glavni Izbornik (GUI)
    # Ovo je petlja koja će vrtjeti aplikaciju dok korisnik ne izađe
    main_menu()

if __name__ == "__main__":
    main()