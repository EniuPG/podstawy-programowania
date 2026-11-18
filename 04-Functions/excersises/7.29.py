# Recursive factorial

def factorial(n):  # definicja funkcji

    if n == 0 or n == 1:  # przypadek podstawowy

        return 1  # 0! i 1! = 1

    return n * factorial(n - 1)  # rekurencja

print(factorial(5))  # 120