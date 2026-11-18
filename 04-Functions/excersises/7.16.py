# Returns nth Fibonacci number

def f(n):  # definicja funkcji

    a = 0  # pierwszy wyraz

    b = 1  # drugi wyraz

    for i in range(n - 1):  # kolejne wyrazy

        a, b = b, a + b  # obliczenie kolejnego

    return a  # zwrócenie wyniku

print(f(5))  # 3

print(f(9))  # 21