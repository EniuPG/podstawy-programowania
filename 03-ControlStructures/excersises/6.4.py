# Password validator

new_password = input("Enter new password: ")  # pobranie hasła

if len(new_password) < 12:  # sprawdzenie długości hasła
    print("Password too short (min. 12 chars)")  # komunikat błędu
else:  # jeśli długość jest poprawna
    print("Password accepted")  # komunikat poprawności