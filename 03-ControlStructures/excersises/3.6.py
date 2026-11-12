# Checks if the given day number of the month is correct

month = int(input("Enter month number (1..12): "))  # pobranie numeru miesiąca
day = int(input("Enter the day number of the month: "))  # pobranie numeru dnia

day_ok = False  # początkowo dzień jest niepoprawny

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # miesiące z 31 dniami
    if day >= 1 and day <= 31:  # sprawdzenie zakresu dni
        day_ok = True  # dzień poprawny

elif month == 4 or month == 6 or month == 9 or month == 11:  # miesiące z 30 dniami
    if day >= 1 and day <= 30:  # sprawdzenie zakresu dni
        day_ok = True  # dzień poprawny

elif month == 2:  # luty
    if day >= 1 and day <= 28:  # sprawdzenie zakresu dni
        day_ok = True  # dzień poprawny

message = f"Day {day} for the month {month}"  # przygotowanie komunikatu

if day_ok:  # jeśli dzień jest poprawny
    print(f"{message} is correct")  # komunikat poprawności
else:  # jeśli dzień jest błędny
    print(f"{message} is incorrect")  # komunikat błędu