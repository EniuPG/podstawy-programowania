# Checking whether the number entered from the keyboard is even or odd

number = int(input("Enter number: "))  # pobranie liczby od użytkownika

if number % 2 == 0:  # sprawdzenie czy reszta z dzielenia przez 2 wynosi 0
    print(f"{number} is even")  # komunikat o liczbie parzystej
else:  # jeśli liczba nie jest parzysta
    print(f"{number} is odd")  # komunikat o liczbie nieparzystej