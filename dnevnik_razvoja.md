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