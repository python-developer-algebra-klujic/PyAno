import os
from services.scales.scale_service import ScaleService
from core.scales.scales import Scale

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_scales(scales):
    print("\n--- POPIS LJESTVICA ---")
    print(f"{'ID':<5} {'Naziv':<20} {'Opis':<40}")
    print("-" * 70)
    if not scales:
        print("Nema spremljenih ljestvica.")
    else:
        for scale in scales:
            desc = scale.description if scale.description else ""
            if len(desc) > 37: desc = desc[:37] + "..."
            print(f"{scale.id:<5} {scale.name:<20} {desc:<40}")
    print("-" * 70)

def add_new_scale():
    print("\n--- DODAVANJE NOVE LJESTVICE ---")
    name = input("Unesite naziv ljestvice (npr. C Major): ").strip()
    if not name:
        print("Naziv ne može biti prazan.")
        return
    description = input("Unesite opis (opcionalno): ").strip()
    
    new_scale = Scale(name=name, description=description)
    service = ScaleService()
    service.create(new_scale)
    print(f"\n✅ Uspješno dodana ljestvica: {name}")

def delete_scale():
    id_str = input("Unesite ID ljestvice za brisanje: ").strip()
    try:
        scale_id = int(id_str)
        service = ScaleService()
        if service.delete(scale_id):
             print(f"✅ Ljestvica ID {scale_id} je obrisana.")
        else:
             print(f"❌ Nije pronađeno.")
    except ValueError:
        print("ID mora biti broj.")

def scales_menu():
    service = ScaleService()
    while True:
        clear_screen()
        print("UPRAVLJANJE LJESTVICAMA")
        print("=" * 30)
        print("1. Prikaži sve ljestvice")
        print("2. Dodaj novu ljestvicu")
        print("3. Obriši ljestvicu")
        print("x. Povratak")
        print("-" * 30)
        
        choice = input("Odabir: ").strip().lower()
        
        if choice == '1':
            display_scales(service.get_all())
            input("Enter...")
        elif choice == '2':
            add_new_scale()
            input("Enter...")
        elif choice == '3':
            delete_scale()
            input("Enter...")
        elif choice == 'x':
            break