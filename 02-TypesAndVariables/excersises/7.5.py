# Program sprawdzający czy samochód jest z Krakowa

car_number = input("Enter car registration number: ")   # Wczytanie numeru

is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"  # Sprawdzenie prefiksu

print(f"Car is from Krakow: {is_krakow}")   # Wyświetlenie wyniku