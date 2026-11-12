# Simple calculator

number1 = float(input("Enter first number: "))  # pobranie pierwszej liczby
number2 = float(input("Enter second number: "))  # pobranie drugiej liczby
operator = input("Enter operator (+,-,*,/): ")  # pobranie działania

if operator == "+":  # sprawdzenie dodawania
    result = number1 + number2  # wykonanie dodawania
elif operator == "-":  # sprawdzenie odejmowania
    result = number1 - number2  # wykonanie odejmowania
elif operator == "*":  # sprawdzenie mnożenia
    result = number1 * number2  # wykonanie mnożenia
elif operator == "/":  # sprawdzenie dzielenia
    result = number1 / number2  # wykonanie dzielenia
else:  # nieznany operator
    result = "Error"  # komunikat błędu

print(f"{number1} {operator} {number2} = {result}")  # wyświetlenie wyniku

#2 + 3
#2 * 4
#3 - 5
#5 * 6