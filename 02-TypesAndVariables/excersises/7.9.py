# Program sprawdzający czy wylosowano 1 lub 6

import random                         # Import modułu random

dice = random.randint(1, 6)          # Losowanie liczby od 1 do 6

special = dice == 1 or dice == 6     # Sprawdzenie warunku

print(f"Dice rolled: {dice}")         # Wyświetlenie wyniku rzutu

print(f"Special number (1 or 6): {special}")  # Informacja o liczbie specjalnej