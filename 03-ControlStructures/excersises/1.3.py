# Checking whether a car exceeded the speed limit

speed_limit = 140  # ograniczenie prędkości na autostradzie
car_speed = int(input("Enter car speed (km/h): "))  # pobranie prędkości samochodu

if car_speed > speed_limit:  # sprawdzenie czy prędkość jest większa od limitu
    print(f"Your speed is {car_speed} km/h")  # wyświetlenie aktualnej prędkości
    print("Warning: speed limit exceeded!!")  # komunikat o przekroczeniu limitu