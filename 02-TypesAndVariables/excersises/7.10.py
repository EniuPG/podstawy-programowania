# Program pozwalający zgadnąć wynik rzutu kostką

import random                          # Import modułu random

# COMPUTER TURN

computer = random.randint(1, 6)        # Komputer losuje liczbę

# YOUR TURN

you = int(input("Guess the dice value (1-6): "))  # Użytkownik podaje liczbę

won = computer == you                  # Sprawdzenie czy użytkownik zgadł

print(f"Computer rolled: {computer}")  # Wyświetlenie liczby komputera

print(f"You guessed: {you}")           # Wyświetlenie liczby gracza

print(f"You won: {won}")               # Informacja o wygranej