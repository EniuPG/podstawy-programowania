# Checking the type of number

number = int(input("Enter a number: "))  # pobranie liczby

if number > 0:  # sprawdzenie czy liczba jest dodatnia
    print(f"Number {number} is positive")  # komunikat dla liczby dodatniej
elif number < 0:  # sprawdzenie czy liczba jest ujemna
    print(f"Number {number} is negative")  # komunikat dla liczby ujemnej
else:  # jeśli liczba jest równa zero
    print("Number is 0")  # komunikat dla zera