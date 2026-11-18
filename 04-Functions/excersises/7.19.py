# Sum of repeated digits

def f(number):  # definicja funkcji

    digits = str(number)  # zamiana na tekst

    total = 0  # suma

    for digit in digits:  # przejście po cyfrach

        if digits.count(digit) > 1:  # sprawdzenie powtórzenia

            total += int(digit)  # dodanie cyfry

    return total  # zwrócenie wyniku

print(f(1027))  # 0

print(f(230335))  # 9

print(f(513553007))  # 21