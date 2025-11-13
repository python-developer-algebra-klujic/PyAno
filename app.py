from config import AppConfig
from infrastructure.base_repository import BaseRepository
from core.pianos.piano_categories import PianoCategory


def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    # Kreiraj db repo i pokreni GUI
    repo = BaseRepository()
    repo.db_seed()
    # Uporaba repozitorija na nacin:
    #   repo.ModelRepository.crud_methods
    #   Primjer za modele: Piano, PianoCategory
    #   repo.Piano.create(new_piano)
    #   repo.PianoCategory.create(new_piano_category)
    piano_category = PianoCategory(name='acoustic')
    piano_category = repo.piano_category_repo.add(piano_category)
    print(piano_category)


if __name__ == "__main__":
    main()
