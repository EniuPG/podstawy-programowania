# Returns numbers from 1 to n as string

def f(n):  # definicja funkcji

    result = ""  # pusty napis

    for i in range(1, n + 1):  # liczby od 1 do n

        result += str(i)  # dodanie liczby

    return result  # zwrócenie wyniku

print(f(11))  # 1234567891011

print(f(4))  # 1234