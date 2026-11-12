# Prime numbers

N = int(input("How many prime numbers: "))  # liczba liczb pierwszych

count = 0  # znalezione liczby pierwsze

number = 2  # pierwsza liczba do sprawdzenia

while count < N:  # dopóki nie znajdziemy N liczb

    is_prime = True  # zakładamy że liczba jest pierwsza

    for i in range(2, number):  # sprawdzanie dzielników

        if number % i == 0:  # znaleziono dzielnik

            is_prime = False  # liczba nie jest pierwsza

            break  # wyjście z pętli

    if is_prime:  # jeśli liczba pierwsza

        print(number, end=" ")  # wyświetlenie liczby

        count += 1  # zwiększenie licznika

    number += 1  # następna liczba