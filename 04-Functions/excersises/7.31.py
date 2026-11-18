# Recursive power

def power(x, n):  # definicja funkcji

    if n == 0:  # przypadek podstawowy

        return 1  # liczba do potęgi 0

    return x * power(x, n - 1)  # rekurencja

print(power(5, 3))  # 125