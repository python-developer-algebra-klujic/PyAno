import os
from services.tones.tone_service import ToneService
from core.tones.tones import Tone

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_tones(tones):
    print("\n--- POPIS TONOVA ---")
    print(f"{'ID':<5} {'Naziv':<10} {'Opis':<40}")
    print("-" * 60)
    
    if not tones:
        print("Nema spremljenih tonova.")
    else:
        for tone in tones:
            desc = tone.description if tone.description else ""
            if len(desc) > 37:
                desc = desc[:37] + "..."
            print(f"{tone.id:<5} {tone.name:<10} {desc:<40}")
    print("-" * 60)

def add_new_tone():
    print("\n--- DODAVANJE NOVOG TONA ---")
    name = input("Unesite naziv tona (npr. C#, Bb): ").strip()
    if not name:
        print("Naziv ne može biti prazan.")
        return

    description = input("Unesite opis tona (opcionalno): ").strip()
    image_url = input("Unesite URL slike (opcionalno): ").strip()

    new_tone = Tone(name=name, description=description, image_url=image_url)
    
    service = ToneService()
    saved_tone = service.create(new_tone)
    
    print(f"\n✅ Uspješno dodan ton: {saved_tone.name}")

def delete_tone():
    print("\n--- BRISANJE TONA ---")
    id_str = input("Unesite ID tona za brisanje: ").strip()
    try:
        tone_id = int(id_str)
        service = ToneService()
        if service.delete(tone_id):
             print(f"✅ Ton ID {tone_id} je obrisan.")
        else:
             print(f"❌ Greška: Ton s ID-om {tone_id} nije pronađen.")
    except ValueError:
        print("Greška: ID mora biti broj.")

def tones_menu():
    service = ToneService()
    while True:
        clear_screen()
        print("UPRAVLJANJE TONOVIMA")
        print("=" * 30)
        print("1. Prikaži sve tonove")
        print("2. Dodaj novi ton")
        print("3. Obriši ton")
        print("x. Povratak")
        print("-" * 30)
        
        choice = input("Odabir: ").strip().lower()
        
        if choice == '1':
            items = service.get_all()
            display_tones(items)
            input("\nPritisnite Enter za nastavak...")
        elif choice == '2':
            add_new_tone()
            input("\nPritisnite Enter za nastavak...")
        elif choice == '3':
            delete_tone()
            input("\nPritisnite Enter za nastavak...")
        elif choice == 'x':
            break