# Program wykonujący trzy rzuty kostką

import random                          # Import modułu random

dice_roll_1 = random.randint(1, 6)     # Pierwszy rzut

dice_roll_2 = random.randint(1, 6)     # Drugi rzut

dice_roll_3 = random.randint(1, 6)     # Trzeci rzut

total = dice_roll_1 + dice_roll_2 + dice_roll_3   # Suma rzutów

print(f"Dice 1: {dice_roll_1}")        # Wynik pierwszego rzutu

print(f"Dice 2: {dice_roll_2}")        # Wynik drugiego rzutu

print(f"Dice 3: {dice_roll_3}")        # Wynik trzeciego rzutu

print(f"Sum: {total}")                 # Suma oczek