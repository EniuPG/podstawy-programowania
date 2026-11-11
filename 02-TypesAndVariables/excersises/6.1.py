# Program obliczający liczbę znaków w imieniu, nazwisku i pełnym imieniu

name = "Jakub" # Wpisz swoje imię
surname = "Jacewicz" # Wpisz swoje nazwisko

characters_in_name = len(name) # Liczba znaków w imieniu

print(f"Your name has {characters_in_name} characters") # Wynik dla imienia

print(f"Your surname has {len(surname)} characters") # Wynik dla nazwiska

full_name = name + " " + surname # Utworzenie pełnego imienia i nazwiska

print(f"Your full name has {len(full_name)} characters") # Wynik dla pełnego imienia