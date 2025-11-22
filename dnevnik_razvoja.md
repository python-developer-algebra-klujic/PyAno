# Dnevnik Razvoja - PyAno

## Dan 1: Postavljanje temelja (Core, Repozitoriji i Servisi)

Danas je postavljen kompletan "back-end" temelj za aplikaciju PyAno. Fokus je bio na prelasku sa SQLAlchemy pristupa (definiranog u `app.py`) na robusnu, troslojnu arhitekturu koja koristi JSON datoteke za pohranu, kako je i traženo u zadatku.

### 1. Dovršavanje `Core` Sloja (Modeli)

Prvi korak bio je dovršiti definiranje svih modela podataka u `core/` folderu. Ovime smo osigurali da imamo jasnu strukturu za sve entitete u aplikaciji.

* `core/tones/tones.py`
* `core/scales/scales.py`
* `core/circles/circles.py`
* `core/lessons/lessons.py`

### 2. Kreiranje `JsonRepository` (Sloj Infrastrukture)

Ovo je bio ključni i najkompleksniji dio dana. Kreirali smo generičku, "pametnu" klasu `infrastructure/json_repository.py`.

**Zašto je "pametna"?**
* **DRY (Don't Repeat Yourself):** Sva logika za čitanje, pisanje, brisanje i ažuriranje JSON-a napisana je samo *jednom*.
* **Robusno Mapiranje:** Koristili smo `sqlalchemy.inspection` alat (`inspect`) kako bismo sigurno pretvarali rječnike (dict) iz JSON-a u SQLAlchemy modele i obrnuto. Ovo sprječava greške i "smeće" (poput `_sa_instance_state`) u našim podacima.
* **Soft Delete:** Logika za meko brisanje (`is_deleted: true`) ugrađena je direktno u repozitorij.

### 3. Implementacija Specifičnih Repozitorija

Nakon što smo imali generički repozitorij, kreiranje specifičnih repozitorija za svaki model bilo je izuzetno brzo. Svaka od ovih klasa samo nasljeđuje `JsonRepository` i prosljeđuje mu model i putanju do datoteke.

```python
# Primjer: infrastructure/pianos/piano_json_repo.py
class PianoJsonRepository(JsonRepository[Piano]):
    def __init__(self):
        super().__init__(file_path=PIANOS_JSON_FILE, model_class=Piano)

        ## Zadaci za riješiti (Tehnički dug)

Nakon implementacije `Core`, `Infrastructure` i `Service` slojeva (15.11.2025.), identificirane su sljedeće greške koje je potrebno ispraviti prije nastavka rada na GUI-ju:

1.  **KRITIČNO (Import Error):** Pogrešan naziv datoteke za Lekcije.
    * **Datoteka:** `core/lessons/lesons.py`
    * **Problem:** Datoteka treba biti preimenovana u `lessons.py` (s dva 's').
    * **Povezano:** `core/lessons/__init__.py` također treba ažurirati da importira iz `.lessons` nakon preimenovanja.

2.  **KRITIČNO (Syntax Error):** Višak teksta u repozitoriju.
    * **Datoteka:** `infrastructure/pianos/piano_json_repo.py`
    * **Problem:** Na kraju datoteke nalazi se riječ `idemo` koja uzrokuje `SyntaxError`. Potrebno ju je obrisati.

3.  **Manji problem (Dokumentacija):** `README.md` je oštećen.
    * **Datoteka:** `README.md`
    * **Problem:** Sadržaj je pomiješan i neformatiran. Potrebno je zamijeniti sadržaj s čistom verzijom.

    ---

## Dan 2: Implementacija GUI-ja i Finalizacija (16.11.2025.)

Danas je fokus bio na izradi korisničkog sučelja (GUI) i povezivanju svih komponenti sustava.

### 1. Rješavanje Tehničkog Duga (Bug Fixes)
Uspješno su riješeni kritični problemi identificirani prethodnog dana:
* ✅ **Popravak Sintakse:** Uklonjena suvišna riječ `idemo` iz `infrastructure/pianos/piano_json_repo.py`.
* ✅ **Ispravak Importa:** Datoteka `core/lessons/lesons.py` preimenovana je u `lessons.py`, a `__init__.py` je ažuriran. Aplikacija se sada pokreće bez grešaka.

### 2. Implementacija Grafičkog Sučelja (GUI)
Kreiran je robustan sustav konzolnih izbornika unutar `gui/` paketa:
* **Glavni Izbornik (`main_menu.py`):** Služi kao centralna točka navigacije.
* **Pod-izbornici:** Kreirani su zasebni moduli za svaku domenu:
    * `pianos_menu_items.py`: Upravljanje klavirima.
    * `lessons_menu_items.py`: Upravljanje lekcijama.
    * `music_theory/`: Poseban paket za teoriju koji sadrži `tones_menu_items.py` i `scales_menu_items.py`, povezan preko `music_theory_menu_items.py`.

### 3. Integracija Sustava
* **`app.py`:** Ulazna točka aplikacije je ažurirana. Više ne izvršava testni kod za bazu, već inicijalizira `BaseRepository` (za kreiranje JSON datoteka) i odmah pokreće `main_menu()`.
* **JSON Perzistencija:** Potvrđeno je da se svi podaci (Klaviri, Tonovi, Lekcije) uspješno spremaju i čitaju iz `.json` datoteka u `data_store/files/`.

### Zaključak
Projekt je funkcionalan i zadovoljava sve zahtjeve zadatka:
1.  Slojevita arhitektura (Core, Infrastructure, Services, GUI).
2.  Korištenje JSON repozitorija umjesto SQL baze.
3.  Implementirano "meko brisanje" (Soft Delete).