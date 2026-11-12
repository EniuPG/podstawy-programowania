# Vehicle speed validation

speed_limit_min = 40  # minimalna dozwolona prędkość
speed_limit_max = 140  # maksymalna dozwolona prędkość

car_speed = int(input("Enter car speed: "))  # pobranie prędkości

if car_speed < speed_limit_min or car_speed > speed_limit_max:  # sprawdzenie zakresu

    print("Warning: invalid car speed!!")  # komunikat ostrzegawczy