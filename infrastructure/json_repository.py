import json
import os
from typing import List, Optional, Type, TypeVar, Generic, Any, Dict

# Importamo inspect alat iz SQLAlchemy-ja za "pametno" mapiranje
from sqlalchemy.inspection import inspect

# Generički tip T
T = TypeVar('T')


class JsonRepository(Generic[T]):
    """
    Generička klasa za upravljanje podacima spremljenim u JSON datoteke.
    Koristi SQLAlchemy modele za strukturu podataka, ali ih sprema u datotečni sustav.
    """

    def __init__(self, file_path: str, model_class: Type[T]):
        """
        Inicijalizacija repozitorija.

        Args:
            file_path (str): Putanja do .json datoteke.
            model_class (Type[T]): Klasa modela (npr. Piano) s kojom repozitorij radi.
        """
        self.file_path = file_path
        self.model_class = model_class
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Provjerava postoji li datoteka i direktorij. Ako ne, kreira ih."""
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            self._save_data([])

    def _load_data(self) -> List[Dict[str, Any]]:
        """Učitava sirove podatke (listu rječnika) iz JSON datoteke."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_data(self, data: List[Dict[str, Any]]) -> None:
        """Sprema listu rječnika u JSON datoteku."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def _get_next_id(self, data: List[Dict[str, Any]]) -> int:
        """Računa sljedeći ID (auto-increment logika)."""
        if not data:
            return 1
        # Pronađi najveći ID u listi i uvećaj za 1
        return max(item.get('id', 0) for item in data) + 1

    def _dict_to_model(self, data_dict: Dict[str, Any]) -> T:
        """
        Napredna konverzija rječnika u SQLAlchemy model.
        Koristi inspekciju modela da bi filtrirao samo validne stupce.
        """
        # 1. Koristimo 'inspect' da dobijemo definiciju modela
        mapper = inspect(self.model_class)
        
        # 2. Izvučemo nazive svih stvarnih stupaca definiranih u modelu
        # (Ovo sprječava greške ako JSON ima polja koja nisu u modelu, npr. 'is_deleted')
        valid_columns = {c.key for c in mapper.columns}

        # 3. Filtriramo ulazne podatke - zadržavamo samo ono što model prepoznaje
        clean_data = {k: v for k, v in data_dict.items() if k in valid_columns}

        # 4. Instanciramo model. SQLAlchemy modeli podržavaju **kwargs konstruktor.
        return self.model_class(**clean_data)

    def _model_to_dict(self, entity: T) -> Dict[str, Any]:
        """
        Konverzija modela natrag u rječnik za spremanje u JSON.
        """
        mapper = inspect(self.model_class)
        data = {}
        
        # Iteriramo samo kroz definirane stupce modela
        for column in mapper.columns:
            key = column.key
            # Dinamički dohvaćamo vrijednost atributa s objekta
            val = getattr(entity, key)
            data[key] = val
            
        return data

    def get_all(self) -> List[T]:
        """Vraća sve entitete koji nisu obrisani (Soft Delete)."""
        raw_data = self._load_data()
        
        # Filtriraj one koji imaju is_deleted=True
        active_items = [
            item for item in raw_data 
            if not item.get('is_deleted', False)
        ]
        
        return [self._dict_to_model(item) for item in active_items]

    def get_by_id(self, entity_id: int) -> Optional[T]:
        """Dohvaća entitet po ID-u ako postoji i nije obrisan."""
        raw_data = self._load_data()
        
        found_item = next(
            (item for item in raw_data 
             if item.get('id') == entity_id and not item.get('is_deleted', False)), 
            None
        )

        if found_item:
            return self._dict_to_model(found_item)
        return None

    def add(self, entity: T) -> T:
        """Dodaje novi entitet, generira ID i sprema u JSON."""
        all_data = self._load_data()
        
        # Generiraj i dodijeli novi ID
        new_id = self._get_next_id(all_data)
        entity.id = new_id
        
        # Pretvori u rječnik
        entity_dict = self._model_to_dict(entity)
        
        # Dodaj metadata polje za soft delete (koje nije dio modela)
        entity_dict['is_deleted'] = False
        
        all_data.append(entity_dict)
        self._save_data(all_data)
        
        return entity

    def update(self, entity: T) -> Optional[T]:
        """Ažurira postojeći entitet."""
        all_data = self._load_data()
        
        # Pronađi indeks elementa s istim ID-om
        index = -1
        for i, item in enumerate(all_data):
            if item.get('id') == entity.id:
                index = i
                break
        
        if index != -1:
            # Pretvori ažurirani entitet u rječnik
            updated_dict = self._model_to_dict(entity)
            
            # Zadrži status brisanja od originalnog podatka (da ga slučajno ne "oživimo" ili obrišemo)
            original_is_deleted = all_data[index].get('is_deleted', False)
            updated_dict['is_deleted'] = original_is_deleted
            
            all_data[index] = updated_dict
            self._save_data(all_data)
            return entity
            
        return None

    def delete(self, entity_id: int) -> bool:
        """Meko brisanje (postavlja is_deleted na True)."""
        all_data = self._load_data()
        
        found = False
        for item in all_data:
            if item.get('id') == entity_id:
                item['is_deleted'] = True
                found = True
                break
        
        if found:
            self._save_data(all_data)
            return True
            
        return False