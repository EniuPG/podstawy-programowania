# Program sprawdzający zwolnienie z podatku

age = int(input("Enter age: "))   # Wczytanie wieku

no_tax = age <= 26                # Sprawdzenie czy wiek jest mniejszy lub równy 26

print(f"Exemption from paying taxes: {no_tax}")  # Wyświetlenie wyniku