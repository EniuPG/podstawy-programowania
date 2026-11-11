# Program sprawdzający czy drzewo można wyciąć

import math                             # Import modułu matematycznego

circumference = float(input("Enter tree circumference in cm: "))  # Obwód drzewa

diameter = circumference / math.pi      # Obliczenie średnicy

can_cut = diameter >= 50                # Sprawdzenie warunku

print(f"Tree can be cut down: {can_cut}")  # Wyświetlenie wyniku