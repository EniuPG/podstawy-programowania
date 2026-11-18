# Recursive sum of natural numbers

def sum_natural(n):  # definicja funkcji

    if n == 1:  # przypadek podstawowy

        return 1  # suma do 1

    return n + sum_natural(n - 1)  # rekurencja

print(sum_natural(10))  # 55