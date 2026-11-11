# Program sprawdzający poprawność prędkości

speed = int(input("Enter vehicle speed: "))   # Wczytanie prędkości

speed_ok = speed >= 40 and speed <= 140       # Zakres dozwolony

print(f"Speed is valid: {speed_ok}")          # Wyświetlenie wyniku