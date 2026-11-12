# Prints a greeting

name = ""  # początkowo zmienna jest pusta

while name == "":  # wykonuj dopóki nie podano imienia
    name = input("Enter your name: ")  # pobranie imienia

print(f"Hello {name}")  # wyświetlenie powitania