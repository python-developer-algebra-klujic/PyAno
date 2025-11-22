import os
from services.lessons.lesson_service import LessonService
from core.lessons.lessons import Lesson

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lessons(lessons):
    print("\n--- POPIS LEKCIJA ---")
    print(f"{'ID':<5} {'Naziv':<30} {'Video URL':<30}")
    print("-" * 70)
    
    if not lessons:
        print("Nema spremljenih lekcija.")
    else:
        for lesson in lessons:
            # Prikazujemo ID, Naziv i URL (ako postoji)
            url = lesson.video_url if lesson.video_url else "Nema URL-a"
            print(f"{lesson.id:<5} {lesson.name:<30} {url:<30}")
    print("-" * 70)

def add_new_lesson():
    print("\n--- DODAVANJE NOVE LEKCIJE ---")
    name = input("Unesite naziv lekcije: ").strip()
    if not name:
        print("Naziv ne može biti prazan.")
        return

    description = input("Unesite opis lekcije (opcionalno): ").strip()
    video_url = input("Unesite video URL (opcionalno): ").strip()

    # Kreiramo novi objekt Lesson
    new_lesson = Lesson(
        name=name, 
        description=description,
        video_url=video_url
    )
    
    service = LessonService()
    saved_lesson = service.create(new_lesson)
    
    print(f"\n✅ Uspješno dodana lekcija: {saved_lesson.name} (ID: {saved_lesson.id})")

def delete_lesson():
    print("\n--- BRISANJE LEKCIJE ---")
    id_str = input("Unesite ID lekcije za brisanje: ").strip()
    try:
        lesson_id = int(id_str)
        service = LessonService()
        
        if service.delete(lesson_id):
             print(f"✅ Lekcija ID {lesson_id} je obrisana.")
        else:
             print(f"❌ Greška: Lekcija s ID-om {lesson_id} nije pronađena.")
    except ValueError:
        print("Greška: ID mora biti cijeli broj.")

def lessons_menu():
    """Glavna petlja pod-izbornika za lekcije."""
    service = LessonService()
    
    while True:
        clear_screen()
        print("UPRAVLJANJE LEKCIJAMA")
        print("=" * 30)
        print("1. Prikaži sve lekcije")
        print("2. Dodaj novu lekciju")
        print("3. Obriši lekciju")
        print("x. Povratak u glavni izbornik")
        print("-" * 30)
        
        choice = input("Odabir: ").strip().lower()
        
        if choice == '1':
            items = service.get_all()
            display_lessons(items)
            input("\nPritisnite Enter za nastavak...")
        elif choice == '2':
            add_new_lesson()
            input("\nPritisnite Enter za nastavak...")
        elif choice == '3':
            delete_lesson()
            input("\nPritisnite Enter za nastavak...")
        elif choice == 'x':
            break