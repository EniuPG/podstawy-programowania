# Program sprawdzający czy liczba jest parzysta

number = int(input("Enter number: "))   # Wczytanie liczby

even = number % 2 == 0                  # Reszta z dzielenia przez 2 równa 0

print(f"Number is even: {even}")        # Wyświetlenie wyniku