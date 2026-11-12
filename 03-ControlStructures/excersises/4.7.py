# Calculates the sum of even numbers in the range <1,10>

sum = 0  # zmienna przechowująca sumę

for i in range(1, 11):  # liczby od 1 do 10

    if i % 2 != 0:  # sprawdzenie czy liczba jest nieparzysta
        continue  # pominięcie nieparzystych liczb

    sum += i  # dodanie liczby parzystej do sumy

print(f"Sum of even numbers in the range <1,10> is {sum}")  # wyświetlenie wyniku