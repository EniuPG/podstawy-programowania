# Program zamieniający liczbę dziesiętną na binarną i szesnastkową

number = int(input("Enter number: "))   # Wczytanie liczby

binary_number = bin(number)             # Konwersja na system binarny

hexadecimal_number = hex(number)        # Konwersja na system szesnastkowy

print(f"Binary number: {binary_number}")         # Wyświetlenie liczby binarnej

print(f"Hexadecimal number: {hexadecimal_number}") # Wyświetlenie liczby szesnastkowej