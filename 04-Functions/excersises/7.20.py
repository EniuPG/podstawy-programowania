# Returns nth prime number

def f(n):  # definicja funkcji

    count = 0  # licznik liczb pierwszych

    number = 2  # pierwsza liczba do sprawdzenia

    while True:  # pętla nieskończona

        prime = True  # założenie liczby pierwszej

        for i in range(2, number):  # sprawdzanie dzielników

            if number % i == 0:  # znaleziono dzielnik

                prime = False  # liczba nie jest pierwsza

                break  # przerwanie pętli

        if prime:  # jeśli liczba pierwsza

            count += 1  # zwiększenie licznika

            if count == n:  # znaleziono n-tą liczbę

                return number  # zwrócenie wyniku

        number += 1  # następna liczba

print(f(1))  # 2

print(f(5))  # 11