# Program wyświetlający wzrost w cm, stopach i calach

cm = 170                              # Wzrost w centymetrach

total_inches = int(cm / 2.54)         # Zamiana centymetrów na cale

feet = total_inches // 12             # Liczba pełnych stóp

inches = total_inches % 12            # Pozostałe cale

print(f"I am {cm} cm tall, i.e. {feet} feet and {inches} inches")  # Wynik