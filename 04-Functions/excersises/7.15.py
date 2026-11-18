# Checks if at least 3 people were in room

def f(detector):  # definicja funkcji

    people = 0  # aktualna liczba osób

    maximum = 0  # maksymalna liczba osób

    for sign in detector:  # analiza znaków

        if sign == "+":  # wejście osoby

            people += 1  # zwiększenie liczby osób

        elif sign == "-":  # wyjście osoby

            people -= 1  # zmniejszenie liczby osób

        if people > maximum:  # aktualizacja maksimum

            maximum = people

    return maximum >= 3  # sprawdzenie warunku

print(f("+-+++-+---"))  # True

print(f("+-+-+-+-"))  # False

print(f("+-++-+--"))  # False

print(f("+-++-++-+---"))  # True