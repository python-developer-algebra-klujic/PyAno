import os
from services.pianos.piano_service import PianoService
from core.pianos.pianos import Piano
# TODO: Import PianoCategory, PianoType and their services when implementing category/type selection
# from core.pianos.piano_categories import PianoCategory
# from core.pianos.piano_types import PianoType
# from services.pianos.piano_category_service import PianoCategoryService
# from services.pianos.piano_type_service import PianoTypeService

__all__ = ["pianos_menu"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_pianos(pianos):
    print("\n--- POPIS KLAVIRA ---")
    print(f"{'ID':<5} {'Naziv':<30} {'Cijena (EUR)':<15}")
    print("-" * 50)
    for piano in pianos:
        print(f"{piano.id:<5} {piano.name:<30} {piano.price:<15.2f}")
    print("-" * 50)


def add_new_piano():
    print("\n--- DODAVANJE NOVOG KLAVIRA ---")
    name = input("Unesite naziv klavira: ")
    try:
        price = float(input("Unesite cijenu (EUR): "))
    except ValueError:
        print("Greška: Cijena mora biti broj.")
        return

    # Napomena: Za pravu aplikaciju ovdje bismo pitali korisnika da odabere 
    # kategoriju i tip iz liste. Za sada ćemo ostaviti prazno ili hardkodirati
    # radi jednostavnosti, ili možeš implementirati odabir kasnije.
    
    # Primjer jednostavnog kreiranja:
    new_piano = Piano(name=name, price=price)
    
    piano_service = PianoService()
    piano_service.create(new_piano)
    print(f"\nUspješno dodan klavir: {name}")


def delete_piano():
    piano_id_str = input("Unesite ID klavira za brisanje: ")
    try:
        piano_id = int(piano_id_str)
        piano_service = PianoService()
        if piano_service.delete(piano_id):
             print(f"Klavir ID {piano_id} je obrisan.")
        else:
             print(f"Klavir s ID-om {piano_id} nije pronađen.")
    except ValueError:
        print("ID mora biti broj.")


def pianos_menu():
    piano_service = PianoService()
    
    while True:
        clear_screen()
        print("UPRAVLJANJE KLAVIRIMA")
        print("=" * 30)
        print("1. Prikaži sve klavire")
        print("2. Dodaj novi klavir")
        print("3. Obriši klavir")
        print("x. Povratak u glavni izbornik")
        print("-" * 30)
        
        choice = input("Odabir: ").strip().lower()
        
        if choice == '1':
            pianos = piano_service.get_all()
            display_pianos(pianos)
            input("\nPritisnite Enter za nastavak...")
        elif choice == '2':
            add_new_piano()
            input("\nPritisnite Enter za nastavak...")
        elif choice == '3':
            delete_piano()
            input("\nPritisnite Enter za nastavak...")
        elif choice == 'x':
            break
