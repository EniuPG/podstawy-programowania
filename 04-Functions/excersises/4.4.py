# Calculates sum of digits

def sum_digits(number):  # definicja funkcji

    number = abs(number)  # usunięcie znaku minus

    total = 0  # suma cyfr

    for digit in str(number):  # przejście po cyfrach

        total += int(digit)  # dodanie cyfry

    return total  # zwrot wyniku

any_number = int(input("Enter integer number: "))  # pobranie liczby

result = sum_digits(any_number)  # wywołanie funkcji

print(f"The sum of digits in {any_number} is {result}")  # wynik