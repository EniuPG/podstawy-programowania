# Decimal to binary converter

decimal_number = int(input("Enter decimal number: "))  # pobranie liczby

binary_number = ""  # pusty wynik

number = decimal_number  # kopia liczby

while number > 0:  # wykonuj dopóki liczba jest większa od zera

    remainder = number % 2  # obliczenie reszty z dzielenia przez 2

    binary_number = str(remainder) + binary_number  # dopisanie bitu na początek

    number = number // 2  # dzielenie całkowite przez 2

print(f"Decimal number: {decimal_number}")  # wyświetlenie liczby dziesiętnej

print(f"Binary number: {binary_number}")  # wyświetlenie liczby binarnej