# Calculates the number of days in a month

month = int(input("Enter month number (1..12): "))  # pobranie numeru miesiąca

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # miesiące 31-dniowe
    days = 31  # przypisanie 31 dni

elif month == 4 or month == 6 or month == 9 or month == 11:  # miesiące 30-dniowe
    days = 30  # przypisanie 30 dni

elif month == 2:  # luty
    days = 28  # luty ma 28 dni

else:  # nieprawidłowy numer miesiąca
    days = 0  # wartość błędna

print(f"Month {month} has {days} days")  # wyświetlenie wyniku