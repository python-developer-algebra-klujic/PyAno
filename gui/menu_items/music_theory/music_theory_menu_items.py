import os
# Importiramo funkcije iz gornje dvije datoteke
from gui.menu_items.music_theory.tones_menu_items import tones_menu
from gui.menu_items.music_theory.scales_menu_items import scales_menu

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def music_theory_menu():
    while True:
        clear_screen()
        print("GLAZBENA TEORIJA")
        print("=" * 30)
        print("1. Upravljanje Tonovima (Tones)")
        print("2. Upravljanje Ljestvicama (Scales)")
        print("3. Akordi (Uskoro)")
        print("4. Kvintni krug (Uskoro)")
        print("x. Povratak u Glavni Izbornik")
        print("-" * 30)
        
        choice = input("Vaš izbor: ").strip().lower()

        if choice == '1':
            tones_menu()  # Poziva izbornik za tonove
        elif choice == '2':
            scales_menu() # Poziva izbornik za ljestvice
        elif choice == '3':
            print("Implementacija slijedi...")
            input("Enter...")
        elif choice == '4':
            print("Implementacija slijedi...")
            input("Enter...")
        elif choice == 'x':
            break