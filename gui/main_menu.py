"""Main menu module for PyAno application."""
import os
import sys
from pyfiglet import Figlet

# Importi naših pod-izbornika
from gui.menu_items.pianos_menu_items import pianos_menu
from gui.menu_items.lessons_menu_items import lessons_menu
from gui.menu_items.music_theory.music_theory_menu_items import music_theory_menu

__all__ = ["main_menu"]


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu() -> None:
    """Terminal-based main menu for the PyAno application."""
    while True:
        clear_screen()
        # Fancy naslov
        f = Figlet(font='slant')
        print(f.renderText('PyAno'))
        print("=" * 50)
        print("     Music Theory Manager")
        print("=" * 50)
        
        print("\n--- GLAVNI IZBORNIK ---")
        print("1. 🎹 Upravljanje Klavirima (Pianos)")
        print("2. 🎵 Glazbena Teorija (Tones, Scales...)")
        print("3. 📚 Lekcije (Lessons)")
        print("x. Izlaz")
        print("-" * 50)
        
        choice = input("Vaš izbor: ").strip().lower()
        
        if choice == '1':
            pianos_menu()
        elif choice == '2':
            music_theory_menu()  # <--- Sada pozivamo tvoj novi izbornik!
        elif choice == '3':
            lessons_menu()
        elif choice == 'x':
            clear_screen()
            print("\nHvala što koristite PyAno! Doviđenja.")
            sys.exit()
        else:
            print("\nNeispravan odabir. Pokušajte ponovo.")
            input("\nPritisnite Enter za nastavak...")