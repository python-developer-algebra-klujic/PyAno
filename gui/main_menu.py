"""Main menu module for PyAno application."""
import os
import pyfiglet
from gui.menu_items.pianos_menu_items import pianos_menu
from gui.menu_items.lessons_menu_items import lessons_menu

__all__ = ["main_menu"]


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu() -> None:
    """Terminal-based main menu for the PyAno application."""
    while True:
        clear_screen()
        # Display fancy title with pyfiglet
        title = pyfiglet.figlet_format("PyAno", font="slant")
        print(title)
        print("=" * 50)
        print("" * 8 + "Music Theory Manager")
        print("=" * 50)
        print("\n--- GLAVNI IZBORNIK ---")
        print("1. Upravljanje klavirima")
        print("2. Upravljanje tonovima")
        print("3. Upravljanje skalama")
        print("4. Upravljanje akordima")
        print("5. Upravljanje krugovima")
        print("6. Upravljanje lekcijama")
        print("x. Izlaz")
        print("-" * 50)
        
        choice = input("Odabir: ").strip().lower()
        
        if choice == '1':
            pianos_menu()
        elif choice == '2':
            print("\nOpcija u pripremi...")
            input("\nPritisnite Enter za nastavak...")
        elif choice == '3':
            lessons_menu() # <--- Pozivamo funkciju
        elif choice == '4':
            print("\nOpcija u pripremi...")
            input("\nPritisnite Enter za nastavak...")
        elif choice == '5':
            print("\nOpcija u pripremi...")
            input("\nPritisnite Enter za nastavak...")
        elif choice == '6':
            print("\nOpcija u pripremi...")
            input("\nPritisnite Enter za nastavak...")
        elif choice == 'x':
            clear_screen()
            print("\nHvala što koristite PyAno!")
            break
        else:
            print("\nNeispravan odabir. Pokušajte ponovo.")
            input("\nPritisnite Enter za nastavak...")