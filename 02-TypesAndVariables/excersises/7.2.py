# Program sprawdzający długość hasła

password = input("Enter password: ")   # Pobranie hasła

password_ok = len(password) >= 8       # Sprawdzenie czy hasło ma minimum 8 znaków

print(f"Password length is valid: {password_ok}")   # Wyświetlenie wyniku