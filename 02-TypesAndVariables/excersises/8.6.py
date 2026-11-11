# Program obliczający koszt transportu

distance = int(input("Enter distance in km: "))           # Dystans w kilometrach

fuel_price = float(input("Enter fuel price per liter: ")) # Cena paliwa

fuel_consumption = float(input("Enter fuel consumption per 100 km: ")) # Spalanie

total_fuel_consumption = distance * fuel_consumption / 100  # Zużyte paliwo

total_cost = total_fuel_consumption * fuel_price           # Koszt przejazdu

print(f"Fuel used: {total_fuel_consumption:.2f} liters")  # Ilość paliwa

print(f"Transport cost: {total_cost:.2f}")                # Koszt transportu