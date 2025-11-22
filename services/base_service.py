from typing import Generic, TypeVar, List, Optional
from infrastructure.json_repository import JsonRepository

# Generički tip T (npr. Piano, Tone...)
T = TypeVar('T')

class BaseService(Generic[T]):
    """
    Bazna klasa za sve servise.
    Sadrži osnovnu poslovnu logiku koja je zajednička za sve modele.
    """

    def __init__(self, repository: JsonRepository[T]):
        """
        Servis prima repozitorij s kojim će raditi.
        Time odvajamo logiku servisa od načina pohrane (Dependency Injection princip).
        """
        self.repository = repository

    def create(self, item: T) -> T:
        """Kreiraj novi entitet."""
        # Ovdje bismo mogli dodati validaciju prije spremanja (npr. je li cijena < 0)
        return self.repository.add(item)

    def get_all(self) -> List[T]:
        """Dohvati sve entitete."""
        return self.repository.get_all()

    def get_by_id(self, item_id: int) -> Optional[T]:
        """Dohvati jedan entitet po ID-u."""
        return self.repository.get_by_id(item_id)

    def update(self, item: T) -> Optional[T]:
        """Ažuriraj postojeći entitet."""
        return self.repository.update(item)

    def delete(self, item_id: int) -> bool:
        """Obriši entitet (meko brisanje)."""
        return self.repository.delete(item_id)