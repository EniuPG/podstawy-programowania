# Fuel consumption calculator

driving_mode = input("Enter driving mode (A/M/E): ")  # pobranie trybu jazdy
distance = int(input("Enter distance in km: "))  # pobranie długości trasy

if driving_mode == "A":  # sprawdzenie trybu Auto
    fuel_consumption = 7  # spalanie 7 l/100 km
elif driving_mode == "M":  # sprawdzenie trybu Manual
    fuel_consumption = 9  # spalanie 9 l/100 km
elif driving_mode == "E":  # sprawdzenie trybu Eco
    fuel_consumption = 6  # spalanie 6 l/100 km
else:  # nieprawidłowy tryb
    fuel_consumption = 0  # ustawienie spalania na 0

total_consumption = distance * fuel_consumption / 100  # obliczenie zużytego paliwa

print(f"Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters")  # wyświetlenie wyniku

#distance 200 km, driving mode M (the result should be 18 liters)
#distance 400 km, driving mode A (the result should be 28 liters)
#distance 350 km, driving mode E (the result should be 21 liters)