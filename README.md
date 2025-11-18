# 🎹 PyAno

> **All about pianos and music theory.**

Dobrodošli u **PyAno**, sveobuhvatnu Python aplikaciju za upravljanje podacima o klavirima i teoriji glazbe. Ovaj projekt demonstrira naprednu, višeslojnu arhitekturu softvera, korištenje ORM-a (SQLAlchemy) i hibridnu pohranu podataka (SQLite + JSON).

---

## 🚀 Kako pokrenuti projekt

Slijedite ove korake kako biste postavili projekt na svom lokalnom računalu.

### 1. Priprema okruženja

Preporučuje se korištenje virtualnog okruženja (`venv`) za izolaciju zavisnosti projekta.

**🐧 Linux (POP OS, Ubuntu) / 🍎 macOS**
```bash
# 1. Kreirajte virtualno okruženje
python3 -m venv venv

# 2. Aktivirajte okruženje
source venv/bin/activate

# 1. Kreirajte virtualno okruženje
python -m venv venv

# 2. Aktivirajte okruženje
.\venv\Scripts\activate

pip install -r requirements.txt

python app.py

Modul,Opis
core/,"Domenski Modeli. Ovdje žive Python klase (npr. Piano, Tone, Scale) koje predstavljaju stvarne entitete. Ovi modeli nasljeđuju SQLAlchemy Base klasu."
infrastructure/,"Pristup Podacima. Sadrži konfiguraciju baze i Repozitorije. Repozitoriji (npr. piano_repo.py) sadrže metode za CRUD operacije (Create, Read, Update, Delete)."
services/,Poslovna Logika. Ovaj sloj povezuje GUI i Repozitorije. Ovdje se donose odluke i obrađuju podaci prije spremanja ili prikazivanja.
gui/,"Korisničko Sučelje. Kod zadužen za interakciju s korisnikom (izbornici, tablice, unos podataka)."
data_store/,Pohrana. Fizička lokacija podataka: • db/py_ano.db (SQLite baza)• files/*.json (JSON datoteke)

from sqlalchemy import Column, Integer, String
from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT

class Tone(Base):
    __tablename__ = "tones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(NAME_LENGHT), unique=True, index=True, nullable=False)

    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        return f'Tone {self.name}'

        PyAno
├── app.py                  # Main entry point
├── config.py               # Global configuration
├── requirements.txt        # Project dependencies
├── core/                   # Models (Piano, Tone, Scale...)
├── infrastructure/         # Repositories (SQL & JSON)
├── services/               # Business logic services
├── gui/                    # User Interface menus
└── data_store/             # Database and JSON storage

✅ Zadaci (Roadmap)

Trenutni fokus razvoja projekta:

    [x] Kreirati klase za sve modele unutar core paketa (Tone, Scale, Circle, Lesson).

    [ ] Kreirati klase repozitorija za pohranu modela unutar .json datoteka.

        [ ] Format naziva: naziv_modela.json.

    [ ] Kreirati Servise za svaki model koji pozivaju CRUD metode iz JSON repozitorija.

    [ ] Implementirati GUI izbornike za interakciju s korisnikom.

    [ ] Implementirati Soft Delete (brisanje označava podatak kao "obrisan", ali ga ne uklanja fizički).
# 🎹 PyAno

> **All about pianos and music theory.**

Dobrodošli u **PyAno**, sveobuhvatnu Python aplikaciju za upravljanje podacima o klavirima i teoriji glazbe. Ovaj projekt demonstrira naprednu, višeslojnu arhitekturu softvera, korištenje ORM-a (SQLAlchemy) i hibridnu pohranu podataka (SQLite + JSON).

---

## 🚀 Kako pokrenuti projekt

Slijedite ove korake kako biste postavili projekt na svom lokalnom računalu.

### 1. Priprema okruženja

Preporučuje se korištenje virtualnog okruženja (`venv`) za izolaciju zavisnosti projekta.

**🐧 Linux (POP OS, Ubuntu) / 🍎 macOS**
```bash
# 1. Kreirajte virtualno okruženje
python3 -m venv venv

# 2. Aktivirajte okruženje
source venv/bin/activate

🪟 Windows
PowerShell

# 1. Kreirajte virtualno okruženje
python -m venv venv

# 2. Aktivirajte okruženje
.\venv\Scripts\activate

2. Instalacija zavisnosti

Nakon što aktivirate okruženje, instalirajte potrebne biblioteke:
Bash

pip install -r requirements.txt

3. Pokretanje aplikacije

Pokrenite glavnu aplikaciju:
Bash

python app.py

🏗️ Arhitektura Aplikacije

Projekt je organiziran u jasne slojeve radi lakšeg održavanja i proširivanja.
Modul	Opis
core/	Domenski Modeli. Ovdje žive Python klase (npr. Piano, Tone, Scale) koje predstavljaju stvarne entitete.
infrastructure/	Pristup Podacima. Sadrži logiku za pohranu podataka. Trenutno koristi JSON repozitorije za spremanje podataka u datoteke.
services/	Poslovna Logika. Ovaj sloj povezuje GUI i Repozitorije. Ovdje se donose odluke i obrađuju podaci prije spremanja.
gui/	Korisničko Sučelje. Konzole izbornici za interakciju s korisnikom.
data_store/	Pohrana. Fizička lokacija podataka (files/*.json).

✅ Status Projekta

Svi zadaci iz plana razvoja su uspješno realizirani:

    [x] Modeli: Kreirane klase u core paketu (Tone, Scale, Circle, Lesson, Piano).

    [x] Repozitoriji: Implementiran generički JsonRepository i specifični repozitoriji za sve modele.

    [x] Servisi: Kreiran servisni sloj za poslovnu logiku.

    [x] GUI: Implementiran glavni izbornik i pod-izbornici za upravljanje podacima.

    [x] Soft Delete: Podaci se ne brišu trajno, već se označavaju kao obrisani (is_deleted: true).

    