# Calculates the sum of even numbers from 1 to N

N = 10  # górna granica zakresu
sum_even = 0  # suma liczb parzystych
i = 1  # licznik

while i <= N:  # wykonuj dopóki i nie przekroczy N

    if i % 2 == 0:  # sprawdzenie czy liczba jest parzysta
        sum_even += i  # dodanie liczby do sumy

    i += 1  # przejście do następnej liczby

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")  # wyświetlenie wyniku